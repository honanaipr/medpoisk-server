from sqlalchemy import UUID, BigInteger, Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

from ..database import Base
from .utils import generate_uuid


class Product(Base):
    __tablename__ = "product"

    id = Column(UUID, primary_key=True, default=generate_uuid)
    title = Column(String)
    min_amount = Column(Integer)
    barcode = Column(BigInteger)
    positions = relationship("Position", back_populates="product")
    picture_url: Mapped[str | None]
