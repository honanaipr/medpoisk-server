from pydantic import BaseModel, ConfigDict
from uuid import UUID


class RoomBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    number: int

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id: UUID
