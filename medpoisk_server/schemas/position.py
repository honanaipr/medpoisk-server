from pydantic import BaseModel, ConfigDict
from uuid import UUID
from .product import Product, ProductCreate
from .place import Place, PlaceCreate


class PositionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product: Product
    amount: int
    place: Place

class PositionCreate(PositionBase):
    product: ProductCreate|UUID
    amount: int
    place: PlaceCreate|UUID

class Position(PositionBase):
    id: UUID