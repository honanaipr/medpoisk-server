from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base
from .place_model import Place
from .product_model import Product


class Inventory(Base):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    place_id: Mapped[int] = mapped_column(ForeignKey("place.id"))
    amount: Mapped[int]

    product: Mapped[Product] = relationship()
    place: Mapped[Place] = relationship()
