from pydantic.type_adapter import TypeAdapter
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas
from .division import flatten_divisions


def get_employee_by_username(
    username: str, session: Session
) -> schemas.EmployeePrivate:
    stmt = select(models.Employee).where(models.Employee.username == username)
    db_employee = session.scalar(stmt)
    return schemas.EmployeePrivate.model_validate(db_employee)


def get_roles_by_employee_id(
    employee_id: int, session: Session
) -> list[schemas.RoleInDivision]:
    stmt = select(models.Privilage).where(models.Privilage.employee_id == employee_id)
    results = session.scalars(stmt)
    flatten_results = []
    for result in results:
        if result.role_name == schemas.Role.director:
            flatten_results.append(
                schemas.RoleInDivision(
                    division=result.division,
                    role_name=schemas.Role.director,
                    inherited=False,
                )
            )
            flatten_results.extend(
                [
                    schemas.RoleInDivision(
                        division=division,
                        role_name=schemas.Role.director,
                        inherited=True,
                    )
                    for division in flatten_divisions([result.division])[1:]
                ]
            )
        else:
            flatten_results.append(result)
    return TypeAdapter(list[schemas.RoleInDivision]).validate_python(flatten_results)
