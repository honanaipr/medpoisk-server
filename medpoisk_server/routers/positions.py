from fastapi import APIRouter, Depends, HTTPException
from ..crud import get_positions, create_position, update_position
from .. import schemas
from ..dependencies import get_db
from sqlalchemy.orm import Session
from .. import exceptions
from sqlalchemy.exc import SQLAlchemyError
import uuid

router = APIRouter(
    prefix="/positions",
    tags=["positions"],
)

@router.get("/", response_model=list[schemas.Position])
async def read_positions(db: Session = Depends(get_db)):
    db_positions = get_positions(db)
    return db_positions

@router.get("/{place_id}/{product_id}", response_model=list[schemas.Position])
async def read_positions_by_id(place_id: uuid.UUID|None=None, product_id: uuid.UUID|None=None, db: Session = Depends(get_db)):
    db_positions = get_positions(db, product_id=product_id, place_id=place_id)
    return db_positions

@router.put("/", response_model=list[schemas.Position])
async def add_positions(positions: list[schemas.PositionCreate],db: Session = Depends(get_db)):
    db_positions =[]
    for position in positions:
        db_position = create_position(db, position)
        db_positions.append(db_position)
    db.commit()
    return db_positions

@router.patch("/", response_model=list[schemas.Position]|None)
async def write_off_positions(position_updates: list[schemas.PositionUpdate], db: Session = Depends(get_db)):
        db_positions =[]
        for position_update in position_updates:
            try:
                db_position = update_position(db, position_update)
                if db_position:
                    db_positions.append(db_position)
            except exceptions.WriteOffMoreThenExist:
                raise HTTPException(status_code=400, detail="An attempt to write off more than exist")
            except SQLAlchemyError as e:
                try:
                    db_position = create_position(db, schemas.PositionCreate.model_validate(position_update) )
                    db_positions.append(db_position)
                except SQLAlchemyError as e:
                    raise HTTPException(status_code=400, detail=str(e))
        db.commit()
        return db_positions
        
