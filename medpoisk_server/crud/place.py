from typing import Iterable
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas


def get_places(
    db: Session, product_id: UUID | None = None, skip: int = 0, limit: int = 100
) -> Iterable[models.Place]:
    stmt = select(models.Place)
    if product_id:
        stmt = (
            stmt.join(models.Position)
            .join(models.Product)
            .where(models.Product.id == product_id)
        )
    stmt = stmt.offset(skip).limit(limit)
    return db.scalars(stmt)


def get_place(
    db: Session, place_name: str | None = None, place_id: UUID | None = None
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
