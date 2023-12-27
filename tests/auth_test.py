from fastapi.testclient import TestClient

from medpoisk_server.main import app
from medpoisk_server.security import jwt_decode

client = TestClient(app)


def get_token() -> str:
    data = data = {
        "grant_type": "",
        "username": "petrovna_rus",
        "password": "petrovna_rus",
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }
    response = client.post("/api/v0/auth/login", data=data)
    return response.json()["access_token"]


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
    assert jwt_decode(response.json()["access_token"]).username
    assert jwt_decode(response.json()["access_token"]).roles
    assert jwt_decode(response.json()["access_token"]).roles[0].division
    assert jwt_decode(response.json()["access_token"]).roles[0].role_name


def test_refresh_token():
    response = client.post(
        "/api/v0/auth/refresh", cookies={"Authorization": f"Bearer {get_token()}"}
    )
    assert response.status_code == 200
    assert response.json()["access_token"]
    assert response.json()["token_type"] == "bearer"
    assert response.cookies["refreshToken"]
