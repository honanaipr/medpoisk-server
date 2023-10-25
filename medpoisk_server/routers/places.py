from fastapi import APIRouter, Depends, HTTPException

from pydantic import BaseModel
from uuid import uuid4, UUID
from faker import Faker

# import faker_commerce


class Place(BaseModel):
    id: UUID
    title: str

    def __hesh__(self):
        return self.id


router = APIRouter(
    prefix="/places",
    tags=["places"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

fake = Faker()
Faker.seed(0)

fake_places_db = [
    Place(
        id=uuid4(),
        title=fake.word(),
    )
    for n in range(5)
]


@router.get("/")
async def read_items() -> list[Place]:
    return fake_places_db


@router.get("/{place_id}")
async def read_item(place_id: UUID) -> Place:
    for item in fake_places_db:
        if item.id == place_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# @router.put("/")
# async def update_item(item: Place):
#     try:
#         try:
#             index = fake_places_db.index(item)
#         except ValueError as e:
#             pass
#         else:
#             del fake_places_db[index]
#         fake_places_db.append(item)
#     except Exception as e:
#         raise HTTPException(status_code=500)
