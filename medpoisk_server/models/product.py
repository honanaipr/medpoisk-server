from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .place import Place
else:
    Place = "Place"
from ..database import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str]
    # min_amount = Column(Integer)
    description: Mapped[str]
    barcode = Column(BigInteger)
    positions = relationship("Position", back_populates="product")
    places: Mapped[list[Place]] = relationship(
        "Place", back_populates="products", secondary="inventory"
    )
    # picture_url: Mapped[str | None]
