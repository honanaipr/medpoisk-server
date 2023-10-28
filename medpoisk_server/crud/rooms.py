from sqlalchemy.orm import Session
from uuid import UUID
from .. import models, schemas


def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()

def get_room(db: Session, room_number: int):
        return db.query(models.Room).where(models.Room.number == room_number).one()

def create_room(db: Session, room: schemas.RoomCreate):
    db_room = models.Room(**room.model_dump())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    
    return schemas.Room(**db_room.__dict__)