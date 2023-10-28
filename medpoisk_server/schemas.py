from pydantic import BaseModel, ConfigDict
from uuid import uuid4, UUID

class PlaceBase(BaseModel):
    title: str

class PlaceCreate(PlaceBase):
    pass

class PlacePublick(PlaceBase):
    pass

class Place(PlaceBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID


class ProductBase(BaseModel):
    title: str
    min_amount: int
    barcode: int

class ProductCreate(ProductBase):
    pass

class ProductPublick(ProductBase):
    amount: int

class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID


class PositionBase(BaseModel):
    product: Product
    amount: int
    place: Place

class PositionCreate(PositionBase):
    pass

class PositionPublick(PositionBase):
    product: ProductBase
    place: PlacePublick

class Position(PositionBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
