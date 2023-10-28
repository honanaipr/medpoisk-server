from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, BigInteger
from sqlalchemy.orm import relationship
from .database import engine

from .database import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

# class Room(Base):
#     __tablename__ = "rooms"

#     id = Column(UUID, primary_key=True, index=True, default=generate_uuid)
#     number = Column(String, index=True)

# class Doctor(Base):
#     __tablename__ = "doctors"

#     id = Column(UUID, primary_key=True, index=True, default=generate_uuid)
#     name = Column(String, index=True)

class Place(Base):
    __tablename__ = "places"

    id = Column(UUID, primary_key=True, default=generate_uuid)
    title = Column(String, index=True)

    positions = relationship("Position", back_populates="place")


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID, primary_key=True, default=generate_uuid)
    title = Column(String)
    min_amount = Column(Integer)
    barcode = Column(BigInteger)
    positions = relationship("Position", back_populates='product')


class Position(Base):
    __tablename__ = "positions"
    
    id = Column(UUID, primary_key=True, default=generate_uuid)
    product = relationship("Product", back_populates='positions')
    amount = Column(Integer)
    place = relationship("Place", back_populates="positions")
    
    
    place_id = Column(UUID, ForeignKey("places.id"))
    product_id = Column(UUID, ForeignKey("products.id"))

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
