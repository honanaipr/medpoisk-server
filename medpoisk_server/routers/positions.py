from fastapi import APIRouter, Depends, HTTPException
from ..crud import get_positions
from ..schemas import PositionPublick


router = APIRouter(
    prefix="/positions",
    tags=["positions"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[PositionPublick])
async def read_positions():
    db_positions = get_positions(db)
    return db_positions

from ..crud import init_positions
from ..database import SessionLocal
db = SessionLocal()
init_positions(db)
