from fastapi.testclient import TestClient

from medpoisk_server.main import app

client = TestClient(app)


def test_get_token():
    data = data = {
        "grant_type": "",
        "username": "ivanov92",
        "password": "ivanov92",
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }
    response = client.post("/api/v0/auth/login", data=data)
    assert response.status_code == 200
    assert response.json()["access_token"]
    assert response.json()["token_type"] == "bearer"
    assert response.cookies["refreshToken"]


def test_refresh_token():
    response = client.post("/api/v0/auth/refresh")
    assert response.status_code == 200
    assert response.json()["access_token"]
    assert response.json()["token_type"] == "bearer"
    assert response.cookies["refreshToken"]
