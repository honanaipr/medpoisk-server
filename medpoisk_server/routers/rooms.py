from fastapi import APIRouter, Depends, HTTPException

from pydantic import BaseModel
from uuid import uuid4, UUID
from faker import Faker

# import faker_commerce


class Room(BaseModel):
    id: UUID
    number: str

    def __hesh__(self):
        return self.id


router = APIRouter(
    prefix="/rooms",
    tags=["rooms"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

fake = Faker()
Faker.seed(0)

fake_rooms_db = [
    Room(
        id=uuid4(),
        number=fake.building_number(),
    )
    for n in range(5)
]


@router.get("/")
async def read_items() -> list[Room]:
    return fake_rooms_db


@router.get("/{item_id}")
async def read_item(item_id: UUID) -> Room:
    for room in fake_rooms_db:
        if room.id == item_id:
            return room
    raise HTTPException(status_code=404, detail="Room not found")
