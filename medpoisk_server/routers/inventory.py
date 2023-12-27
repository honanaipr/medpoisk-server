from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, dependencies, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)


@router.get("/", response_model=list[schemas.InventoryItmePublick])
async def get_all_inventory(
    db: Annotated[Session, Depends(get_db)],
    token_data: Annotated[
        schemas.TokenData, Depends(dependencies.get_verified_token_data)
    ],
):
    return crud.get_inventory(db, token_data)
