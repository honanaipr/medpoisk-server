from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

if TYPE_CHECKING:
    from .division_model import Division
    from .product_model import Product
else:
    Division = "Division"
    Product = "Product"


class Limit(Base):
    __tablename__ = "limit"

    id: Mapped[int] = mapped_column(primary_key=True)
    division_id: Mapped[int] = mapped_column(ForeignKey("division.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    min_amount: Mapped[int]

    division: Mapped[Division] = relationship("Division")
    product: Mapped[Product] = relationship("Product")
