from pydantic import BaseModel, ConfigDict
from uuid import UUID
from .division import DivisionPublick


class RoomBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    division: DivisionPublick


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    id: int
