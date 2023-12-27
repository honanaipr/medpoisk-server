import pytest
from fastapi.testclient import TestClient
from pydantic.type_adapter import TypeAdapter

from medpoisk_server import schemas
from medpoisk_server.main import app
from medpoisk_server.security import jwt_decode

from .auth_test import get_token

client = TestClient(app)


def test_get_profile_me():
    token = get_token()
    response = client.get(
        "/api/v0/profile/me", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    employee = schemas.EmployeePublicDetailed.model_validate(
        response.json(), from_attributes=True
    )
    assert employee
    assert employee
    assert employee.id
    assert employee.username
    assert employee.email
    assert employee.first_name
    assert employee.middle_name
    assert employee.last_name


@pytest.mark.parametrize("role, num_employees", zip(schemas.Role, [5, 2, 0]))
def test_get_staff(role, num_employees):
    token = get_token(role)
    response = client.get(
        "/api/v0/profile/staff", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    employees = TypeAdapter(list[schemas.EmployeePublic]).validate_python(
        response.json(), from_attributes=True
    )
    assert len(employees) == num_employees


def test_get_staff_for_director_for_concrete_division():
    token = get_token(schemas.Role.director)
    response = client.get(
        "/api/v0/profile/staff",
        headers={"Authorization": f"Bearer {token}"},
        params={
            "division_id": [
                role.division.id for role in jwt_decode(token).roles if role.inherited
            ]
        },
    )
    assert response.status_code == 200
    employees = TypeAdapter(list[schemas.EmployeePublic]).validate_python(
        response.json(), from_attributes=True
    )
    assert len(employees) == 2
