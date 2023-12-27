from pydantic import BaseModel

from .division import DivisionPublick
from .product import ProductShortPublick


class LimitPublick(BaseModel):
    division: DivisionPublick
    product: ProductShortPublick
    min_amount: int
