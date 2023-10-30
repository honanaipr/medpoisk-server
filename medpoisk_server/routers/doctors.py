from fastapi import APIRouter, Depends, HTTPException
from ..schemas import Doctor, Doctor, DoctorCreate
from uuid import UUID
from .. import crud
from ..dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound

router = APIRouter(
    prefix="/doctors",
    tags=["doctors"],
)


@router.get("/", response_model=list[Doctor])
async def get_all_doctors(db: Session = Depends(get_db)):
    return crud.get_doctors(db)

@router.put("/", response_model=Doctor)
async def add_new_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_doctor(db, doctor)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Doctor {doctor.name} already exist!") from e
