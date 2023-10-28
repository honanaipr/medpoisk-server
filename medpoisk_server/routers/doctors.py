from fastapi import APIRouter, Depends, HTTPException
from ..schemas import DoctorPublick, Doctor
from uuid import UUID
from ..crud.doctors import get_doctors
from ..dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/doctors",
    tags=["doctors"],
    # responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[DoctorPublick])
async def read_items(db: Session = Depends(get_db)):
    return get_doctors(db)


# @router.get("/{doctor_id}")
# async def read_item(doctor_id: UUID) -> Doctor:
#     for doctor in fake_doctors_db:
#         if doctor.id == doctor_id:
#             return doctor
#     raise HTTPException(status_code=404, detail="Doctor not found")

from ..crud import init_doctors
from ..database import SessionLocal
db = SessionLocal()
init_doctors(db)
