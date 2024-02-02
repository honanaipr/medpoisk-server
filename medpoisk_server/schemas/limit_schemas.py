from pydantic import BaseModel


class LimitPublick(BaseModel):
    division_id: int
    product_id: int
    min_amount: int
