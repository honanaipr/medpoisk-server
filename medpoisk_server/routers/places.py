from fastapi import APIRouter, Depends, HTTPException
from ..schemas import Place, PlaceCreate
from ..dependencies import get_db
from sqlalchemy.orm import Session
from .. import crud
from sqlalchemy.exc import IntegrityError, NoResultFound

router = APIRouter(
    prefix="/places",
    tags=["places"],
)

@router.get("/", response_model=list[Place])
async def get_all_places(db: Session = Depends(get_db)):
    return crud.get_places(db)

@router.put("/", response_model=Place)
async def add_new_place(place: PlaceCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_place(db, place)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Place {place.title} already exist!") from e
