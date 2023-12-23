from pydantic import BaseModel, ConfigDict
from uuid import UUID


class DoctorBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


class DoctorCreate(DoctorBase):
    pass


class Doctor(DoctorBase):
    id: UUID
