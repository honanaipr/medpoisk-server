from fastapi import APIRouter, Depends, HTTPException
from ..crud import get_positions, create_position, update_position
from ..schemas import Position, PositionCreate, PositionPublick
from .. import schemas
from ..dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound

router = APIRouter(
    prefix="/positions",
    tags=["positions"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[PositionPublick])
async def read_positions(db: Session = Depends(get_db)):
    db_positions = get_positions(db)
    return db_positions

@router.put("/", response_model=Position)
async def add_position(positions: list[PositionCreate],db: Session = Depends(get_db)):
    for position in positions:
        try:
            db_positions = create_position(db, position)
            return db_positions
        except IntegrityError as e:
            try:
                db_positions = update_position(db, position)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Integrity error!") from e


from ..crud import init_positions
from ..database import SessionLocal
db = SessionLocal()
init_positions(db)
