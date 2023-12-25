from fastapi import APIRouter, Depends, HTTPException
from ..schemas import Place, PlaceCreate
from ..dependencies import get_db
from sqlalchemy.orm import Session
from .. import crud
from sqlalchemy.exc import IntegrityError, NoResultFound
import uuid

router = APIRouter(
    prefix="/place",
    tags=["place"],
)


@router.get("/", response_model=list[Place])
async def get_all_places(
    product_id: uuid.UUID | None = None, db: Session = Depends(get_db)
):
    return crud.get_places(db, product_id)


@router.put("/", response_model=Place)
async def add_new_place(place: PlaceCreate, db: Session = Depends(get_db)):
    try:
        db_place = crud.create_place(db, place)
    except IntegrityError as e:
        raise HTTPException(
            status_code=400, detail=f"Place {place.title} already exist!"
        ) from e
    db.commit()
    return db_place
