from uuid import UUID

from pydantic import BaseModel, ConfigDict

from .place import Place


class ProductBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    min_amount: int
    barcode: int


class ProductCreate(ProductBase):
    pass


class ProductPublick(ProductBase):
    id: UUID
    amount: int
    places: list[Place]
    picture_url: str | None


class Product(ProductBase):
    id: UUID
