from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, BigInteger

from ..database import Base
import uuid
from .utils import generate_uuid

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(UUID, primary_key=True, default=generate_uuid)
    name = Column(String, unique=True)