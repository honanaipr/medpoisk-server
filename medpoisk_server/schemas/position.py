from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from .place import Place, PlaceCreate
from .product import Product, ProductCreate


class PositionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product: Product
    amount: int
    place: Place


class PositionCreate(PositionBase):
    product: ProductCreate | None = Field(default=None)
    product_id: UUID | None = Field(default=None)
    amount: int
    place: PlaceCreate | None = Field(default=None)
    place_id: UUID | None = Field(default=None)


class PositionUpdate(BaseModel):
    product_id: UUID = Field(default=None)
    amount: int
    place_id: UUID = Field(default=None)


class Position(PositionBase):
    id: UUID
