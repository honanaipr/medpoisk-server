from pydantic import BaseModel

from .place import PlaceShortPublick
from .product import ProductShortPublick


class InventoryItmePublick(BaseModel):
    product: ProductShortPublick
    place: PlaceShortPublick
    amount: int
