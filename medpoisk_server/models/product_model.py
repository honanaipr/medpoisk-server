from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .picture_model import Picture

if TYPE_CHECKING:
    from .place_model import Place
else:
    Place = "Place"
from ..database import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]
    barcode: Mapped[int | None] = mapped_column(BigInteger)
    places: Mapped[list[Place]] = relationship(
        "Place", back_populates="products", secondary="inventory"
    )
    pictures: Mapped[list[Picture]] = relationship(
        "Picture", back_populates="product", cascade="all, delete"
    )
