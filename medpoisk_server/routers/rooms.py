from fastapi import APIRouter, Depends, HTTPException
from ..schemas import RoomPublick, Room, RoomCreate
from uuid import UUID
from ..crud import get_rooms, get_room, create_room
from ..dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound


router = APIRouter(
    prefix="/rooms",
    tags=["rooms"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[RoomPublick])
async def read_rooms(db: Session = Depends(get_db)):
    return get_rooms(db)


@router.get("/{room_number}", response_model=Room)
async def read_room(room_number: int, db: Session = Depends(get_db)):
    try:
        return get_room(db, room_number)
    except NoResultFound as e:
        raise HTTPException(status_code=400, detail=f"Room number {room_number} not exist!") from e

@router.put("/", response_model=Room)
async def new_room(room: RoomCreate, db: Session = Depends(get_db)):
    try:
        return create_room(db, room)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Room number {room.number} already exist!") from e

from ..crud import init_rooms
from ..database import SessionLocal
db = SessionLocal()
init_rooms(db)
