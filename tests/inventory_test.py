from fastapi.testclient import TestClient
from pydantic.type_adapter import TypeAdapter

from medpoisk_server import schemas
from medpoisk_server.app import app

from .auth_test import get_token

client = TestClient(app)


def test_get_inventory():
    token = get_token()
    response = client.get(
        "/api/v0/inventory", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()
    inventory = TypeAdapter(list[schemas.InventoryItmePublick]).validate_python(
        response.json(), from_attributes=True
    )
    assert inventory
    assert inventory[0].product
    assert inventory[0].product.id
    assert inventory[0].product.title
    assert inventory[0].place
    assert inventory[0].place.id
    assert inventory[0].place.title
    assert inventory[0].amount
