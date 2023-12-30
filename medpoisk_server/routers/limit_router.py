from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, dependencies, schemas

router = APIRouter(
    prefix="/limit",
    tags=["limit"],
)


@router.get("/", response_model=list[schemas.LimitPublick])
async def get_all_doctors(
    db: Annotated[Session, Depends(dependencies.get_db)],
    divisions: Annotated[
        list[schemas.DivisionPublick], Depends(dependencies.get_auntificated_divisions)
    ],
):
    return crud.get_min_amounts(db, [division.id for division in divisions])
