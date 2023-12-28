from fastapi.testclient import TestClient
from pydantic.type_adapter import TypeAdapter

from medpoisk_server import schemas
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
