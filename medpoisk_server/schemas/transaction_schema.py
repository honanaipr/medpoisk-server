from decimal import Decimal

from pydantic import BaseModel


class Transaction(BaseModel):
    id: int
    product_id: int
    invoice_id: int | None
    from_place_id: int | None
    to_place_id: int | None
    room_id: int | None
    user_id: int
    amount: int
    price: Decimal
