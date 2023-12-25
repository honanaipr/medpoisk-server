from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .. import crud
from ..dependencies import get_db
from ..schemas import Doctor, DoctorCreate

router = APIRouter(
    prefix="/doctor",
    tags=["doctor"],
)


@router.get("/", response_model=list[Doctor])
async def get_all_doctors(db: Session = Depends(get_db)):
    return crud.get_doctors(db)


@router.put("/", response_model=Doctor)
async def add_new_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    try:
        db_doctor = crud.create_doctor(db, doctor)
    except IntegrityError as e:
        raise HTTPException(
            status_code=400, detail=f"Doctor {doctor.name} already exist!"
        ) from e
    db.commit()
    return db_doctor
