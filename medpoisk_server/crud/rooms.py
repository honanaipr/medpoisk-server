from sqlalchemy.orm import Session
from .. import models, schemas


def get_rooms(db: Session, skip: int = 0, limit: int = 100) -> list[models.Room]:
    return db.query(models.Room).offset(skip).limit(limit).all()

def get_room(db: Session, room_number: int) -> models.Room:
        return db.query(models.Room).where(models.Room.number == room_number).one()

def create_room(db: Session, room: schemas.RoomCreate) -> models.Room:
    db_room = models.Room(**room.model_dump())
    db.add(db_room)
    db.flush()
    db.refresh(db_room)
    return db_room
