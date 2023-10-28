from sqlalchemy.orm import Session

from .. import models
# from ..schemas.doctor import Doctor as model_doctor

def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doctor).offset(skip).limit(limit).all()