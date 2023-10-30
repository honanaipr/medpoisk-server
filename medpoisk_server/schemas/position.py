from pydantic import BaseModel, ConfigDict
from uuid import uuid4, UUID
from .product import Product, ProductBase, ProductId, ProductCreate
from .place import Place, PlacePublick, PlaceCreate, PlaceId


class PositionBase(BaseModel):
    product: Product
    amount: int
    place: Place

class PositionCreate(PositionBase):
    product: ProductCreate|ProductId
    amount: int
    place: PlaceCreate|PlaceId


class PositionPublick(PositionBase):
    product: ProductBase
    place: PlacePublick

class Position(PositionBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID