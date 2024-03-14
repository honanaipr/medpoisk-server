from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy import types as sa_types
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base
from .division_model import Division
from .product_model import Product


class Balance(Base):
    __tablename__ = "balance"

    id: Mapped[int] = mapped_column(primary_key=True)
    division_id: Mapped[int] = mapped_column(ForeignKey("division.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    avg_price: Mapped[Decimal] = mapped_column(sa_types.DECIMAL)
    amount: Mapped[int]

    division: Mapped[Division] = relationship("Division", back_populates="balance")
    product: Mapped[Product] = relationship("Product")
