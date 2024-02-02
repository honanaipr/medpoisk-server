from pydantic import BaseModel


class MoveRequest(BaseModel):
    from_place_id: int
    to_place_id: int
    product_id: int
    amount: int
