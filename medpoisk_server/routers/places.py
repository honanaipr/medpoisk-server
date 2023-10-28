from fastapi import APIRouter, Depends, HTTPException
from ..schemas import PlacePublick
from ..dependencies import get_db
from sqlalchemy.orm import Session
from ..crud import get_places

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

from ..crud import init_places
from ..database import SessionLocal
db = SessionLocal()
init_places(db)
