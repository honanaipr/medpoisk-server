from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, BigInteger
from sqlalchemy.orm import relationship
from ..database import engine

from ..database import Base
import uuid
from .utils import generate_uuid

class Place(Base):
    __tablename__ = "places"

    id = Column(UUID, primary_key=True, default=generate_uuid)
    title = Column(String, unique=True)

    positions = relationship("Position", back_populates="place")