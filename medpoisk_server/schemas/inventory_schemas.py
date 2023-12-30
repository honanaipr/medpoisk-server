from pydantic import BaseModel

from .place_schemas import PlaceShortPublick
from .product_schemas import ProductShortPublick


class InventoryItmePublick(BaseModel):
    product: ProductShortPublick
    place: PlaceShortPublick
    amount: int
