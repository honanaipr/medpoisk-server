from sqlalchemy import (
    ForeignKey,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from ..database import Base
import uuid
from .utils import generate_uuid
import sqlalchemy as sa


class Position(Base):
    __tablename__ = "position"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=generate_uuid)
    product = relationship("Product", back_populates="positions")
    amount: Mapped[int] = mapped_column(default=0)
    place = relationship("Place", back_populates="positions")

    place_id: Mapped[uuid.UUID] = mapped_column(sa.UUID, ForeignKey("place.id"))
    product_id: Mapped[uuid.UUID] = mapped_column(sa.UUID, ForeignKey("product.id"))
