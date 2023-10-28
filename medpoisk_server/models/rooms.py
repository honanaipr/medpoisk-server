from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, BigInteger
from sqlalchemy.orm import relationship
from ..database import engine

from ..database import Base
import uuid
from .utils import generate_uuid

class Room(Base):
    __tablename__ = "rooms"

    id = Column(UUID, primary_key=True, default=generate_uuid)
    number = Column(Integer)