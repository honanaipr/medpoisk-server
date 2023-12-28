from uuid import UUID

from pydantic.type_adapter import TypeAdapter
from sqlalchemy import UUID as db_UUID
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .. import models, schemas


def get_product(
    db: Session, product_name: str | None = None, product_barcode: int | None = None
):
    if product_name is not None:
        return (
            db.query(models.Product).where(models.Product.title == product_name).one()
        )
    elif product_barcode is not None:
        return (
            db.query(models.Product)
            .where(models.Product.barcode == product_barcode)
            .one()
        )
    else:
        raise ValueError("place_name or place_id mast be specified")


def get_product_amount(db: Session, product_id: db_UUID):
    return (
        db.query(func.coalesce(func.sum(models.Position.amount), 0))
        .join(models.Product)
        .where(models.Product.id == product_id)
        .scalar()
    )


def get_product_places(db: Session, product_id: db_UUID):
    return (
        db.query(models.Place)
        .join(models.Position)
        .join(models.Product)
        .where(models.Product.id == product_id)
        .all()
    )


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.flush()
    db.refresh(db_product)
    return db_product


def set_product_picture_url(db: Session, id: UUID, url: str):
    stmt = select(models.Product).where(models.Product.id == id)
    db_product = db.scalars(stmt).one()
    db_product.picture_url = url


def delete_products(db: Session, id: UUID):
    stmt = select(models.Product).where(models.Product.id == id)
    db_product = db.scalar(stmt)
    db.delete(db_product)


def get_all_products(db: Session) -> list[schemas.ProductPublick]:
    stmt = select(models.Product)
    return TypeAdapter(list[schemas.ProductPublick]).validate_python(
        db.scalars(stmt), from_attributes=True
    )
