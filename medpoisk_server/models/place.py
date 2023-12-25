from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship

from ..database import Base
from .utils import generate_uuid


class Place(Base):
    __tablename__ = "place"

    id = Column(UUID, primary_key=True, default=generate_uuid)
    title = Column(String, unique=True)

    positions = relationship("Position", back_populates="place")
