from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, BigInteger, CheckConstraint
from sqlalchemy.orm import relationship
from ..database import engine

from ..database import Base
import uuid
from .utils import generate_uuid


class Position(Base):
    __tablename__ = "positions"
    
    id = Column(UUID, primary_key=True, default=generate_uuid)
    product = relationship("Product", back_populates='positions')
    amount = Column(Integer, CheckConstraint("amount >= 0"), default=0)
    place = relationship("Place", back_populates="positions")
    
    
    place_id = Column(UUID, ForeignKey("places.id"))
    product_id = Column(UUID, ForeignKey("products.id"))