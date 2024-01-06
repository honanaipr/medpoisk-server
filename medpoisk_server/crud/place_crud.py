from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas


def get_places(
    db: Session,
    division_ids: list[int],
) -> Iterable[models.Place]:
    stmt = select(models.Place).where(models.Place.division_id.in_(division_ids))
    return db.scalars(stmt)


def get_place(
    db: Session, place_name: str | None = None, place_id: int | None = None
) -> models.Place:
    if place_name is not None:
        return db.query(models.Place).where(models.Place.title == place_name).one()
    elif place_id is not None:
        return db.query(models.Place).where(models.Place.id == place_id).one()
    else:
        raise ValueError("place_name or place_id mast be specified")


def create_place(db: Session, place: schemas.PlaceCreate) -> models.Place:
    db_place = models.Place(**place.model_dump())
    db.add(db_place)
    db.flush()
    db.refresh(db_place)
    return db_place
