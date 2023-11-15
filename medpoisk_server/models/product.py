from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, BigInteger
from sqlalchemy.orm import relationship

from ..database import Base
import uuid
from .utils import generate_uuid

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID, primary_key=True, default=generate_uuid)
    title = Column(String)
    min_amount = Column(Integer)
    barcode = Column(BigInteger)
    positions = relationship("Position", back_populates='product')