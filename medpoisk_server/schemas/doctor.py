from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DoctorBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


class DoctorCreate(DoctorBase):
    pass


class Doctor(DoctorBase):
    id: UUID
