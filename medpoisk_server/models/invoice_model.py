from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Date

from ..database import Base

if TYPE_CHECKING:
    from .transaction_model import Transaction
else:
    Transaction = "Transaction"


class Invoice(Base):
    __tablename__ = "invoice"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]
    date: Mapped[datetime] = mapped_column(Date)

    transactions: Mapped[list[Transaction]] = relationship(
        "Transaction", back_populates="invoice"
    )
