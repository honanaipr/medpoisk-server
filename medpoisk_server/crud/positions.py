from sqlalchemy.orm import Session

from .. import models, schemas

def get_positions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Position).offset(skip).limit(limit).all()

def create_position(db: Session, place: schemas.ProductCreate):
    db_place = models.Product(**place.model_dump())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place