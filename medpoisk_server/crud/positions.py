from sqlalchemy.orm import Session
from .. import models, schemas
from sqlalchemy import select
from .. import exceptions
from typing import Iterable
import uuid

def get_positions(db: Session, product_id: uuid.UUID|None=None, place_id: uuid.UUID|None=None, skip: int = 0, limit: int = 100) -> Iterable[models.Position]:
    stmt = select(models.Position)
    if product_id:
        stmt = stmt.join(models.Product).join(models.Place).where(models.Product.id == product_id).where(models.Place.id == place_id)
    stmt = stmt.offset(skip).limit(limit)
    return db.scalars(stmt)

def create_position(db: Session, position: schemas.PositionCreate):
    if position.place:
        db_place = models.Place(**position.place.model_dump())
        db.add(db_place)
    else:
        db_place = db.get_one(models.Place, position.place_id)
    
    if position.product:
        db_product = models.Product(**position.product.model_dump())
        db.add(db_product)
    else:
        db_product = db.get_one(models.Product, position.product_id)
    
    db.flush()
    db_position  = models.Position(amount=position.amount, product=db_product, place=db_place)
    db.add(db_position)
    db.flush()
    db.refresh(db_position)
    return db_position

def update_position(db: Session, position: schemas.PositionUpdate):
    db_position = db.scalars(
        select(models.Position).
        join(models.Product).
        join(models.Place).
        where(models.Product.id == position.product_id).
        where(models.Place.id == position.place_id)
        ).one()
    db_position.amount += position.amount
    if db_position.amount < db_position.product.min_amount:
        db.rollback()
        raise exceptions.WriteOffMoreThenMinimal
    db.flush()
    db.refresh(db_position)
    return db_position
