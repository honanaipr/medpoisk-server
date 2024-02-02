from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models


def get_balance(db: Session, division_ids: list[int]) -> Iterable[models.Balance]:
    stmt = select(models.Balance).where(models.Balance.division_id.in_(division_ids))
    return db.scalars(stmt)
