from pydantic.type_adapter import TypeAdapter
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas


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
    return TypeAdapter(list[schemas.RoleInDivision]).validate_python(list(results))
