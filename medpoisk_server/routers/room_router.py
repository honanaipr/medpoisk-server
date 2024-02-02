from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .. import crud, dependencies, schemas
from ..dependencies import get_db
from ..schemas import Room, RoomCreate

router = APIRouter(
    prefix="/room",
    tags=["room"],
)


@router.get("/", response_model=list[Room])
async def get_all_rooms(
    db: Annotated[Session, Depends(get_db)],
    user: Annotated[
        schemas.EmployeePrivate, Depends(dependencies.get_auntificated_employee)
    ],
):
    return crud.get_rooms(db, user)


@router.put("/", response_model=schemas.RoomBublick)
async def add_new_room(room: RoomCreate, db: Session = Depends(get_db)):
    try:
        db_room = crud.create_room(db, room)
    except IntegrityError as e:
        raise HTTPException(
            status_code=400, detail=f"Room title {room.title} already exist!"
        ) from e
    db.commit()
    return db_room
