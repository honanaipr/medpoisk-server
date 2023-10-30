from sqlalchemy.orm import Session
from sqlalchemy import func, select
from sqlalchemy import UUID as db_UUID
from uuid import UUID
from .. import models, schemas

def get_products(db: Session, skip: int = 0, limit: int = 100) -> list[models.Product]:
    stmt = select(models.Product).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())

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

def get_publick_products(db: Session, skip: int = 0, limit: int = 100) -> list[schemas.Product]:
    db_products = get_products(db, skip=skip, limit=limit)
    products = []
    for db_product in db_products:
        places = []
        for place in get_product_places(db, db_product.id):        
            places.append(schemas.Place.model_validate(place))
        product = schemas.ProductPublick(**db_product.__dict__, amount=get_product_amount(db, db_product.id), places=places)
        products.append(product)
    return products

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product