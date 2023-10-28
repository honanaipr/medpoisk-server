from fastapi import APIRouter, Depends, HTTPException
from ..schemas import RoomPublick
from uuid import UUID
from ..crud import get_rooms
from ..dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/rooms",
    tags=["rooms"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[RoomPublick])
async def read_items():
    return get_rooms(db)


# @router.get("/{item_id}")
# async def read_item(item_id: UUID) -> Room:
#     for room in fake_rooms_db:
#         if room.id == item_id:
#             return room
#     raise HTTPException(status_code=404, detail="Room not found")

from ..crud import init_rooms
from ..database import SessionLocal
db = SessionLocal()
init_rooms(db)
