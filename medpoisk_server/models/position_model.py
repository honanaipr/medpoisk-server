from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class Position(Base):
    __tablename__ = "position"

    id: Mapped[int] = mapped_column(primary_key=True)
    product = relationship("Product", back_populates="positions")
    amount: Mapped[int] = mapped_column(default=0)
    place = relationship("Place", back_populates="positions")

    place_id: Mapped[int] = mapped_column(Integer, ForeignKey("place.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"))
