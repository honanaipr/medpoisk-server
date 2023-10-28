from pydantic import BaseModel, ConfigDict
from uuid import uuid4, UUID


class RoomBase(BaseModel):
    number: int

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id: UUID

class RoomPublick(RoomBase):
    pass
