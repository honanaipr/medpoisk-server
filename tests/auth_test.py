from functools import lru_cache

import pytest
from fastapi.testclient import TestClient

from medpoisk_server import schemas
from medpoisk_server.app import app
from medpoisk_server.security import jwt_decode

client = TestClient(app)


@lru_cache
def get_token(role: schemas.Role = schemas.Role.director) -> str:
    data = data = {
        "grant_type": "",
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }
    if role == schemas.Role.manager:
        data.update(
            {
                "username": "petrovna_rus",
                "password": "petrovna_rus",
            }
        )
    elif role == schemas.Role.director:
        data.update(
            {
                "username": "ivanov92",
                "password": "ivanov92",
            }
        )
    elif role == schemas.Role.doctor:
        data.update(
            {
                "username": "anna_kovaleva",
                "password": "anna_kovaleva",
            }
        )
    response = client.post("/api/v0/auth/login", data=data)
    assert response.status_code == 200
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
    token = schemas.Token.model_validate(response.json(), from_attributes=True)
    assert token.access_token
    assert token.token_type == "bearer"
    assert response.cookies["refreshToken"]
    token_data = jwt_decode(token.access_token)
    assert token_data
    assert token_data.username
    assert token_data.roles
    assert token_data.roles[0].division
    assert token_data.roles[0].role_name


def test_refresh_token():
    response = client.post(
        "/api/v0/auth/refresh", cookies={"Authorization": f"Bearer {get_token()}"}
    )
    assert response.status_code == 200
    token = schemas.Token.model_validate(response.json(), from_attributes=True)
    assert token
    assert token.token_type == "bearer"
    assert response.cookies["refreshToken"]


def test_get_token_vrong_cred():
    data = data = {
        "grant_type": "",
        "username": "qweqweqwe",
        "password": "123123123",
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }
    response = client.post("/api/v0/auth/login", data=data)
    assert response.status_code == 401
    with pytest.raises(KeyError):
        assert response.json()["access_token"]
    with pytest.raises(KeyError):
        assert response.json()["token_type"]


def test_get_token_for_director():
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
    token = schemas.Token.model_validate(response.json(), from_attributes=True)
    token_data = jwt_decode(token.access_token)
    assert token_data.roles
    assert token_data.roles[0].division.title == "Главный офис"
    assert token_data.roles[0].role_name == schemas.Role.director
    assert not token_data.roles[0].inherited
    assert token_data.roles[1].division.title == "Филиал №1"
    assert token_data.roles[1].role_name == schemas.Role.director
    assert token_data.roles[1].inherited
    assert token_data.roles[2].division.title == "Субфилиал №1"
    assert token_data.roles[2].role_name == schemas.Role.director
    assert token_data.roles[2].inherited
    assert token_data.roles[3].division.title == "Филиал №2"
    assert token_data.roles[3].role_name == schemas.Role.director
    assert token_data.roles[3].inherited
