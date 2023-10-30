from sqlalchemy.orm import Session
from uuid import UUID
from .. import models,schemas


def get_places(db: Session, skip: int = 0, limit: int = 100) -> list[models.Place]:
    return db.query(models.Place).offset(skip).limit(limit).all()

def get_place(db: Session, place_name: str|None = None, place_id: UUID|None = None) -> models.Place:
    if place_name is not None:
        return db.query(models.Place).where(models.Place.title == place_name).one()
    elif place_id is not None:
        return db.query(models.Place).where(models.Place.id == place_id).one()
    else:
        raise ValueError("place_name or place_id mast be specified")

def create_place(db: Session, place: schemas.PlaceCreate, nocommit=True) -> models.Place:
    db_place = models.Place(**place.model_dump())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place
