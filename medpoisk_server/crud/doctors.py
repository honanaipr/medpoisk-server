from sqlalchemy.orm import Session

from .. import models, schemas


def get_doctors(db: Session, skip: int = 0, limit: int = 100) -> list[models.Doctor]:
    return db.query(models.Doctor).offset(skip).limit(limit).all()


def create_doctor(db: Session, doctor: schemas.DoctorCreate) -> models.Doctor:
    db_doctor = models.Doctor(**doctor.model_dump())
    db.add(db_doctor)
    db.flush()
    db.refresh(db_doctor)
    return db_doctor
