from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .division import Division
    from .product import Product
else:
    Division = "Division"
    Product = "Product"
from ..database import Base


class Place(Base):
    __tablename__ = "place"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    division_id: Mapped[int] = mapped_column(ForeignKey("division.id"))

    division: Mapped[Division] = relationship("Division", back_populates="places")

    products: Mapped[Product] = relationship(
        "Product", back_populates="places", secondary="inventory"
    )
    positions = relationship("Position", back_populates="place")
