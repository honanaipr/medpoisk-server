from fastapi import APIRouter, Depends, HTTPException

from pydantic import BaseModel
from uuid import uuid4, UUID
from faker import Faker
from .places import Place, fake_places_db
import random
# import faker_commerce


class Item(BaseModel):
    id: UUID
    heading: str
    amount: int
    min_amount: int
    places: list[Place]

    def __hesh__(self):
        return self.id


router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

fake = Faker()
Faker.seed(0)

fake_items_db = [
    Item(
        id=uuid4(),
        heading=fake.sentence(),
        amount=fake.random_number(digits=2),
        min_amount=fake.random_number(digits=2),
        places=random.sample(fake_places_db, random.randint(a=1, b=3))
    )
    for n in range(10)
]


@router.get("/")
async def read_items() -> list[Item]:
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: UUID) -> Item:
    for item in fake_items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@router.put("/")
async def update_item(item: Item):
    try:
        try:
            index = fake_items_db.index(item)
        except ValueError as e:
            pass
        else:
            del fake_items_db[index]
        fake_items_db.append(item)
    except Exception as e:
        raise HTTPException(status_code=500)
