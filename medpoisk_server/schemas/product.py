from pydantic import BaseModel, ConfigDict
from uuid import UUID
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

class Product(ProductBase):
    id: UUID