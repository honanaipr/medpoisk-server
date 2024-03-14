from typing import Iterable

from pydantic.type_adapter import TypeAdapter
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas


def get_min_amounts(
    db: Session, division_ids: list[int]
) -> Iterable[schemas.LimitPublick]:
    stmt = select(models.Limit).where(models.Limit.division_id.in_(division_ids))
    results = db.scalars(stmt)
    return TypeAdapter(list[schemas.LimitPublick]).validate_python(
        results, from_attributes=True
    )
