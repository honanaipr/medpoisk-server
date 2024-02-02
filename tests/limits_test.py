import pytest
from fastapi.testclient import TestClient
from pydantic.type_adapter import TypeAdapter

from medpoisk_server import schemas
from medpoisk_server.app import app

from .auth_test import get_token

client = TestClient(app)


@pytest.mark.parametrize("role, num_limits", zip(schemas.Role, [4, 4, 4]))
def test_get_limits_for_role(role, num_limits):
    token = get_token(role)
    response = client.get(
        "/api/v0/limit/", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()
    limits = TypeAdapter(list[schemas.LimitPublick]).validate_python(
        response.json(), from_attributes=True
    )
    assert len(limits) == num_limits
    assert limits[0].product_id
    assert limits[0].division_id
    assert limits[0].min_amount
