from sqlalchemy.orm import Session
from .. import schemas
from .. import models
from sqlalchemy import select


def get_employee_by_username(
    username: str, session: Session
) -> schemas.EmployeePrivate | None:
    stmt = select(models.Employee).where(models.Employee.username == username)
    db_employee = session.scalar(stmt)
    if not db_employee:
        return None
    return schemas.EmployeePrivate.model_validate(db_employee)
