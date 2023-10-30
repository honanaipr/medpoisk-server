from sqlalchemy.orm import Session

from .. import models, schemas
from .places import create_place, get_place
from .products import create_product, get_product
from sqlalchemy import select, update
from sqlalchemy.exc import NoResultFound
from uuid import UUID
# from sqlalchemy.dialects.postgresql import UUID as pg_UUID

def get_positions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Position).offset(skip).limit(limit).all()

def create_position(db: Session, position: schemas.PositionCreate):
    match position.place:
        case schemas.PlaceCreate():
            db_place = models.Place(**position.place.model_dump())
            db.add(db_place)
            # db_place = create_place(db, position.place, nocommit=True)
        case UUID():
            # db_place = db.scalars(select(models.Place).where(models.Place.id == pg_UUID(position.place))).one()
            db_place = db.query(models.Place).where(models.Place.id == position.place).one()
    match position.product:
        case schemas.ProductCreate():
            # db_product = create_product(db, position.product)
            db_product = models.Product(**position.product.model_dump())
            db.add(db_product)
        case UUID():
            # db_product = db.execute(select(models.Product).where(models.Product.id == position.product)).one()
            db_product = db.query(models.Product).where(models.Product.id == position.product).one()
    try:
        # db_position = db.query(models.Position).join(models.Product).join(models.Place).where(models.Product.id == db_product.id).where(models.Place.id == db_place.id).one()
        db.execute(update(models.Position).where(models.Position.product_id == db_product.id).where(models.Position.place_id == db_place.id).values(amount=position.amount))
        db_position = db.execute(select(models.Position).where(models.Position.product_id == db_product.id).where(models.Position.place_id == db_place.id)).scalar()
        if not db_position:
            db_position = models.Position(amount=position.amount, place=db_place, product=db_product)
            db.add(db_position)
    except Exception:
        db_position = models.Position(amount=position.amount, place=db_place, product=db_product)
        db.add(db_position)
    db.commit()
    db.refresh(db_position)
    return db_position

def update_position(db: Session, position: schemas.PositionCreate):
    # db_position = models.Position(amount=position.amount, place=db_place, product=db_product)
    
    db_position = select(models.Position).join(models.Product).where(models.Product.barcode == db_product.barcode).one()
    db_position.amount = position.amount
    return db_position