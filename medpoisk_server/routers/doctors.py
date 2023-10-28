from fastapi import APIRouter, Depends, HTTPException
from ..schemas import DoctorPublick, Doctor, DoctorCreate
from uuid import UUID
from ..crud.doctors import get_doctors, get_doctor, create_doctor
from ..dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound

router = APIRouter(
    prefix="/doctors",
    tags=["doctors"],
    # responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[DoctorPublick])
async def read_items(db: Session = Depends(get_db)):
    return get_doctors(db)

@router.get("/{doctor_name}", response_model=Doctor)
async def read_room(doctor_name: str, db: Session = Depends(get_db)):
    try:
        return get_doctor(db, doctor_name)
    except NoResultFound as e:
        raise HTTPException(status_code=400, detail=f"Doctor {doctor_name} not exist!") from e

@router.put("/", response_model=Doctor)
async def new_room(doctor: DoctorCreate, db: Session = Depends(get_db)):
    try:
        return create_doctor(db, doctor)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Doctor {doctor.name} already exist!") from e

from ..crud import init_doctors
from ..database import SessionLocal
db = SessionLocal()
init_doctors(db)
