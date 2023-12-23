from pydantic import BaseModel, ConfigDict
from uuid import UUID


class PlaceBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    id: UUID
