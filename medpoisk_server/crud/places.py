from sqlalchemy.orm import Session

from .. import models,schemas


def get_places(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Place).offset(skip).limit(limit).all()

def get_place(db: Session, place_name: str):
        return db.query(models.Place).where(models.Place.title == place_name).one()

def create_place(db: Session, place: schemas.PlaceCreate):
    db_place = models.Place(**place.model_dump())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    
    return schemas.Place(**db_place.__dict__)