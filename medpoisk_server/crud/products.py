from sqlalchemy.orm import Session
from sqlalchemy import func, Select
from sqlalchemy import UUID as db_UUID
from uuid import UUID
from .. import models, schemas

def get_products(db: Session, skip: int = 0, limit: int = 100) -> list[models.Product]:
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_name: str|None = None, product_barcode: int|None = None):
    if product_name is not None:
        return db.query(models.Product).where(models.Product.title == product_name).one()
    elif product_barcode is not None:
        return db.query(models.Product).where(models.Product.barcode == product_barcode).one()
    else:
        raise ValueError("place_name or place_id mast be specified")

def get_product_amount(db: Session, product_id: db_UUID):
    return db.query(func.coalesce(func.sum(models.Position.amount),0)).join(models.Product).where(models.Product.id == product_id).scalar()

def get_product_places(db: Session, product_id: db_UUID):
    return db.query(models.Place).join(models.Position).join(models.Product).where(models.Product.id == product_id).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product