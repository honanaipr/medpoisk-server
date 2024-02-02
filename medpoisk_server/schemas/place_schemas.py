from pydantic import BaseModel, ConfigDict


class PlaceBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str


class PlaceCreate(PlaceBase):
    title: str
    division_id: int


class Place(PlaceBase):
    id: int


class PlaceIdPublick(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int


class PlaceShortPublick(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str


class PlacePublick(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    division_id: int
