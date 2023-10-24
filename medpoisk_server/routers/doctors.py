from fastapi import APIRouter, Depends, HTTPException

from pydantic import BaseModel
from uuid import uuid4, UUID
from faker import Faker

# import faker_commerce


class Doctor(BaseModel):
    id: UUID
    name: str

    def __hesh__(self):
        return self.id


router = APIRouter(
    prefix="/doctors",
    tags=["doctors"],
    # responses={404: {"description": "Not found"}},
)

fake = Faker()
Faker.seed(0)

fake_doctors_db = [
    Doctor(
        id=uuid4(),
        name=fake.name(),
    )
    for n in range(3)
]


@router.get("/")
async def read_items() -> list[Doctor]:
    return fake_doctors_db


@router.get("/{doctor_id}")
async def read_item(doctor_id: UUID) -> Doctor:
    for doctor in fake_doctors_db:
        if doctor.id == doctor_id:
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")
