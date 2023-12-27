from fastapi.testclient import TestClient

from medpoisk_server.main import app

from .auth_test import get_token

client = TestClient(app)


def test_get_inventory():
    token = get_token()
    response = client.get(
        "/api/v0/inventory", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()
    assert response.json()[0]
    assert response.json()[0]["product"]
    assert response.json()[0]["product"]["id"]
    assert response.json()[0]["product"]["title"]
    assert response.json()[0]["place"]
    assert response.json()[0]["place"]["id"]
    assert response.json()[0]["place"]["title"]
    assert response.json()[0]["amount"]
