from pydantic import BaseModel, ConfigDict
from uuid import uuid4, UUID

class PlaceBase(BaseModel):
    title: str

class PlaceId(BaseModel):
    id: UUID

class PlaceCreate(PlaceBase):
    pass

class PlacePublick(PlaceBase):
    pass

class Place(PlaceBase, PlaceId):
    model_config = ConfigDict(from_attributes=True)
    # id: UUID