from sqlalchemy import Column, String, UUID

from ..database import Base
from .utils import generate_uuid


class Doctor(Base):
    __tablename__ = "doctor"

    id = Column(UUID, primary_key=True, default=generate_uuid)
    name = Column(String, unique=True)
