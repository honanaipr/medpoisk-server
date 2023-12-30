from pydantic import BaseModel

from .division_schemas import DivisionPublick
from .product_schemas import ProductShortPublick


class LimitPublick(BaseModel):
    division: DivisionPublick
    product: ProductShortPublick
    min_amount: int
