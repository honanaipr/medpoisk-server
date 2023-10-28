from pydantic import BaseModel, ConfigDict
from uuid import uuid4, UUID

class PlaceBase(BaseModel):
    title: str

class PlaceCreate(PlaceBase):
    pass

class PlacePublick(PlaceBase):
    pass

class Place(PlaceBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID