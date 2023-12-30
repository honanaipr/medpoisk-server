import re
from pathlib import Path
from typing import BinaryIO
from urllib.parse import quote, urljoin
from uuid import UUID

from pydantic.type_adapter import TypeAdapter
from sqlalchemy import UUID as db_UUID
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .. import models, schemas
from ..config import config


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


def str2slug(input: str) -> str:
    # Remove invalid characters
    valid_chars = re.sub(r"[^\w\s\-_.]", "", input)

    # Replace whitespace with underscores
    valid_filename = re.sub(r"\s+", "_", valid_chars)

    # Trim length to fit within the maximum filename length limit
    max_filename_length = 255
    if len(valid_filename) > max_filename_length:
        valid_filename = valid_filename[:max_filename_length]

    return valid_filename


def product_name_to_file_name(product_name: str, mime_type: str, num: int) -> str:
    extention = mime_type.split("/")[-1]
    return quote(f"{str2slug(product_name)}_{num}.{extention}")


def create_product(
    db: Session,
    product: schemas.ProductCreate,
    input_pictures: list[tuple[BinaryIO, str]],
) -> schemas.ProductPublick:
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.flush()
    db_pictures = [
        models.Picture(
            product_id=db_product.id,
            url=urljoin(
                config.pictures_base_url,
                product_name_to_file_name(str(db_product.id), picture[1], pos),
            ),
        )
        for pos, picture in enumerate(input_pictures, start=1)
        if picture[1].split("/")[0] == "image"
    ]
    db.add_all(db_pictures)
    db.flush()
    written: list[Path] = []
    try:
        for picture in zip(db_pictures, input_pictures):
            path = config.pictures_dir / picture[0].url
            path.touch()
            path.write_bytes(picture[1][0].read())
            written.append(path)
    except OSError:
        for path in written:
            path.unlink()
        raise
    return schemas.ProductPublick.model_validate(db_product, from_attributes=True)


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
