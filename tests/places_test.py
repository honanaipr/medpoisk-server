import pytest
from fastapi.testclient import TestClient
from pydantic.type_adapter import TypeAdapter

from medpoisk_server import schemas
from medpoisk_server.app import app

from .auth_test import get_token

client = TestClient(app)


@pytest.mark.parametrize("role, num_places", zip(schemas.Role, [18, 6, 0]))
def test_get_places_for_role(role, num_places):
    token = get_token(role)
    response = client.get(
        "/api/v0/place/", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json() is not None
    places = TypeAdapter(list[schemas.PlacePublick]).validate_python(
        response.json(), from_attributes=True
    )
    assert len(places) == num_places
    if role is not schemas.Role.doctor:
        assert places[0].title is not None
        assert places[0].id is not None
        assert places[0].division_id is not None
