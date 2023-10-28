from pydantic import BaseModel, ConfigDict
from uuid import uuid4, UUID
from .product import Product, ProductBase
from .place import Place, PlacePublick


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