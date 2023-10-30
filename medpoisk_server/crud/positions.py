from sqlalchemy.orm import Session

from .. import models, schemas
from .places import create_place, get_place
from .products import create_product, get_product
from sqlalchemy import select

def get_positions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Position).offset(skip).limit(limit).all()

def create_position(db: Session, position: schemas.PositionCreate):
    match position.product:
        case schemas.ProductCreate():
            # db_product = create_product(db, position.product)
            db_product = models.Product(**position.product.model_dump())
        case schemas.ProductId():
            db_product = get_product(db, product_id=position.product.id)
    match position.place:
        case schemas.PlaceCreate():
            db_place = models.Place(**position.place.model_dump())
            # db_place = create_place(db, position.place, nocommit=True)
        case schemas.PlaceId():
            db_place = get_place(db, place_id=position.place.id)
    db_position = models.Position(amount=position.amount, place=db_place, product=db_product)
    db.add(db_position)
    db.commit()
    db.refresh(db_position)
    return db_position

def update_position(db: Session, position: schemas.PositionCreate):
    match position.product:
        case schemas.ProductCreate():
            # db_product = create_product(db, position.product)
            db_product = models.Product(**position.product.model_dump())
        case schemas.ProductBarcode():
            db_product = get_product(db, product_id=position.product.barcode)
    match position.place:
        case schemas.PlaceCreate():
            db_place = models.Place(**position.place.model_dump())
            # db_place = create_place(db, position.place, nocommit=True)
        case schemas.PlaceId():
            db_place = get_place(db, place_id=position.place.id)
    db_position = models.Position(amount=position.amount, place=db_place, product=db_product)
    
    db_position = select(models.Position).join(models.Product).where(models.Product.barcode == db_product.barcode).one()
    db_position.amount = position.amount
    return db_position