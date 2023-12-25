from sqlalchemy import select
from sqlalchemy.orm import Session
from .. import models, schemas
from typing import Iterable
from sqlalchemy.orm import aliased


def flatten_divisions(S):
    if not S:
        return S
    return S[:1] + flatten_divisions(S[0].sub_divisions) + flatten_divisions(S[1:])


def get_rooms(db: Session, employee: schemas.EmployeePrivate) -> Iterable[models.Room]:
    db_employee = db.scalars(
        select(models.Employee).where(models.Employee.username == employee.username)
    ).one()
    db_privilages = set([privilage for privilage in db_employee.privilages])
    db_divisions = [privilage.division for privilage in db_privilages]
    db_divisions = flatten_divisions(db_divisions)
    db_rooms = set()
    for division in db_divisions:
        db_rooms.update(division.rooms)
    return db_rooms


def get_room(db: Session, room_title: int) -> models.Room:
    return db.query(models.Room).where(models.Room.title == room_title).one()


def create_room(db: Session, room: schemas.RoomCreate) -> models.Room:
    db_room = models.Room(**room.model_dump())
    db.add(db_room)
    db.flush()
    db.refresh(db_room)
    return db_room
