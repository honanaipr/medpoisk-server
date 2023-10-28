from sqlalchemy.orm import Session

from .. import models, schemas

def get_products(db: Session, skip: int = 0, limit: int = 100) -> list[models.Product]:
    return db.query(models.Product).offset(skip).limit(limit).all()

from sqlalchemy import func, Select
from sqlalchemy import UUID as db_UUID

def get_product_amount(db: Session, product_id: db_UUID):
    return db.query(func.sum(models.Position.amount)).join(models.Product).where(models.Product.id == product_id).scalar()

def create_product(db: Session, place: schemas.ProductCreate):
    db_place = models.Product(**place.model_dump())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place