from fastapi.testclient import TestClient

from medpoisk_server.app import app

from .auth_test import get_token

client = TestClient(app)


def test_get_all_rooms():
    token = get_token()
    response = client.get("/api/v0/room", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()
    assert response.json()[0]
    assert response.json()[0]["id"]
    assert response.json()[0]["title"]
    assert response.json()[0]["division"]
    assert response.json()[0]["division"]["id"]
    assert response.json()[0]["division"]["title"]
