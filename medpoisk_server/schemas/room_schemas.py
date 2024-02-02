from pydantic import BaseModel, ConfigDict

from .division_schemas import DivisionPublick


class RoomBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    division: DivisionPublick


class RoomCreate(BaseModel):
    title: str
    division_id: int


class Room(RoomBase):
    id: int


class RoomBublick(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    division_id: int
