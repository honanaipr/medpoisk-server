from fastapi import APIRouter, Depends, HTTPException
from ..schemas import PlacePublick, Place, PlaceCreate
from ..dependencies import get_db
from sqlalchemy.orm import Session
from ..crud import get_places, get_place, create_place
from sqlalchemy.exc import IntegrityError, NoResultFound

router = APIRouter(
    prefix="/places",
    tags=["places"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[PlacePublick])
async def read_places(db: Session = Depends(get_db)):
    db_places = get_places(db)
    return db_places

@router.get("/{place_title}", response_model=Place)
async def read_room(place_title: str, db: Session = Depends(get_db)):
    try:
        return get_place(db, place_title)
    except NoResultFound as e:
        raise HTTPException(status_code=400, detail=f"Place {place_title} not exist!") from e

@router.put("/", response_model=Place)
async def new_room(place: PlaceCreate, db: Session = Depends(get_db)):
    try:
        return create_place(db, place)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Place {place.title} already exist!") from e

from ..crud import init_places
from ..database import SessionLocal
db = SessionLocal()
init_places(db)
