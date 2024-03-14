from datetime import date

from pydantic import BaseModel

from .. import schemas


class Invoice(BaseModel):
    number: int
    data: date
    transactions: schemas.Transaction
