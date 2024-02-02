from pydantic.type_adapter import TypeAdapter
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas


def flatten_divisions(S):
    if not S:
        return S
    return S[:1] + flatten_divisions(S[0].sub_divisions) + flatten_divisions(S[1:])


def get_staff(
    db: Session, division_ids: list[int], role_name: schemas.Role | None = None
) -> list[schemas.EmployeePublicDetailed]:
    stmt = (
        select(models.Employee)
        .join(models.Employee.privilages)
        .where(models.Privilage.division_id.in_(division_ids))
    )
    if role_name is not None:
        stmt = stmt.where(models.Privilage.role_name == role_name)
    db_employee = db.scalars(stmt)
    return TypeAdapter(list[schemas.EmployeePublicDetailed]).validate_python(
        db_employee, from_attributes=True
    )
