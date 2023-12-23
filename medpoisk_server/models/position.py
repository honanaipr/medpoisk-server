from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    BigInteger,
    CheckConstraint,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from ..database import Base
import uuid
from .utils import generate_uuid
import sqlalchemy as sa


class Position(Base):
    __tablename__ = "positions"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=generate_uuid)
    product = relationship("Product", back_populates="positions")
    amount: Mapped[int] = mapped_column(default=0)
    place = relationship("Place", back_populates="positions")

    place_id: Mapped[uuid.UUID] = mapped_column(sa.UUID, ForeignKey("places.id"))
    product_id: Mapped[uuid.UUID] = mapped_column(sa.UUID, ForeignKey("products.id"))
