# from typing import TYPE_CHECKING

from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base
from .product_model import Product

if TYPE_CHECKING:
    from .invoice_model import Invoice
else:
    Invoice = "Invoice"


class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    invoice_id: Mapped[int | None] = mapped_column(ForeignKey("invoice.id"))

    from_place_id: Mapped[int | None] = mapped_column(ForeignKey("place.id"))
    to_place_id: Mapped[int | None] = mapped_column(ForeignKey("place.id"))

    room_id: Mapped[int | None] = mapped_column(ForeignKey("place.id"))
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))

    amount: Mapped[Decimal]
    price: Mapped[int]

    product: Mapped[Product] = relationship("Product")

    invoice: Mapped[Invoice] = relationship("Invoice", back_populates="transactions")
