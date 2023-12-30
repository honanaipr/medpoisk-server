import filecmp
from pathlib import Path

from fastapi.testclient import TestClient
from pydantic.type_adapter import TypeAdapter

from medpoisk_server import schemas
from medpoisk_server.crud import delete_product
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
    response = client.get(
        "/api/v0/product",
        headers={"Authorization": f"Bearer {token}"},
    )

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
