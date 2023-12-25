from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PlaceBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    id: UUID
