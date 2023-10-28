from sqlalchemy.orm import Session

from .. import models, schemas
# from ..schemas.doctor import Doctor as model_doctor

def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doctor).offset(skip).limit(limit).all()

def get_doctor(db: Session, doctor_name: str):
        return db.query(models.Doctor).where(models.Doctor.name == doctor_name).one()

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.model_dump())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    
    return schemas.Doctor(**db_doctor.__dict__)