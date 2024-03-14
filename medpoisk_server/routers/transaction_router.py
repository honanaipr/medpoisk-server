from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/transaction",
    tags=["transaction"],
)


@router.get("/", response_model=list[schemas.Transaction])
async def get_all_transactions(
    db: Annotated[Session, Depends(get_db)],
):
    return crud.read_transactions(db)


@router.get("/{transaction_id}/", response_model=schemas.Transaction)
async def get_transaction_by_id(
    transaction_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    return crud.read_transaction(db, transaction_id)


@router.post("/", response_model=schemas.RoomBublick)
async def new_transaction(
    transaction: schemas.Transaction, db: Session = Depends(get_db)
):
    return crud.create_transaction(db, transaction)
