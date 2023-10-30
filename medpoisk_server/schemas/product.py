from pydantic import BaseModel, ConfigDict
from uuid import uuid4, UUID
from .place import PlacePublick
class ProductBase(BaseModel):
    title: str
    min_amount: int
    barcode: int

class ProductId(BaseModel):
    id: UUID

class ProductCreate(ProductBase):
    pass

class ProductPublickShort(ProductBase):
    pass

class ProductPublick(ProductBase):
    amount: int
    places: list[PlacePublick]

class Product(ProductBase, ProductId):
    model_config = ConfigDict(from_attributes=True)
    # id: UUID