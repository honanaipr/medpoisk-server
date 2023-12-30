import filecmp
from pathlib import Path

from fastapi.testclient import TestClient
from pydantic.type_adapter import TypeAdapter

from medpoisk_server import schemas
from medpoisk_server.crud import create_product, delete_product, get_all_products
from medpoisk_server.database import SessionLocal
from medpoisk_server.main import app

from .auth_test import get_token

client = TestClient(app)


def test_get_all_products():
    token = get_token()
    response = client.get(
        "/api/v0/product", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()
    products = TypeAdapter(list[schemas.ProductPublick]).validate_python(
        response.json(), from_attributes=True
    )
    assert len(products) == 10
    assert products[0].id
    assert products[0].title
    assert products[0].barcode
    assert products[0].description
    assert products[0].pictures
    assert products[0].pictures[0].url


def test_create_product(cleanup=True):
    token = get_token()
    new_product = schemas.ProductCreate(title="Миромистин", barcode=123)
    files = [
        (
            "pictures",
            (
                "foo.jpeg",
                open(Path(__file__).parent / "assets" / "mock_image.jpeg", "rb"),
                "image/jpeg",
            ),
        ),
        (
            "pictures",
            (
                "bar.jpeg",
                open(Path(__file__).parent / "assets" / "mock_image.jpeg", "rb"),
                "image/jpeg",
            ),
        ),
    ]
    response = client.put(
        "/api/v0/product",
        headers={"Authorization": f"Bearer {token}"},
        data=new_product.model_dump(),
        files=files,
    )
    assert response.status_code == 200
    assert response.json()
    product = schemas.ProductPublick.model_validate(
        response.json(), from_attributes=True
    )
    assert product
    assert product.pictures[0].url
    mock_path = Path(__file__).parent / "assets" / "mock_image.jpeg"

    for picture in product.pictures:
        test_path = Path(__file__).parent.parent / "pictures" / picture.url
        assert filecmp.cmp(mock_path, test_path)

    if cleanup:
        with SessionLocal() as db:
            delete_product(db, product.id)
            db.commit()


def test_delete_product():
    token = get_token()
    new_product = schemas.ProductCreate(title="Тестовый продукт", barcode=123)
    try:
        with SessionLocal() as db:
            new_product = create_product(
                db,
                new_product,
                [
                    (
                        open(
                            Path(__file__).parent / "assets" / "mock_image.jpeg", "rb"
                        ),
                        "image/jpeg",
                    ),
                    (
                        open(
                            Path(__file__).parent / "assets" / "mock_image.jpeg", "rb"
                        ),
                        "image/jpeg",
                    ),
                ],
            )
            db.commit()
        with SessionLocal() as db:
            products = get_all_products(db)
            assert new_product in products
        response = client.delete(
            "/api/v0/product",
            headers={"Authorization": f"Bearer {token}"},
            params={"id": new_product.id},
        )
        assert response.status_code == 200
        with SessionLocal() as db:
            products = get_all_products(db)
            assert new_product not in products
    except Exception:
        with SessionLocal() as db:
            if isinstance(new_product, schemas.ProductPublick):
                delete_product(db, new_product.id)
        raise
