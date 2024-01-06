from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .. import crud, dependencies, schemas
from ..dependencies import get_db
from ..schemas import Place, PlaceCreate

router = APIRouter(
    prefix="/place",
    tags=["place"],
)


@router.get("/", response_model=list[schemas.PlacePublick])
async def get_all_places(
    db: Annotated[Session, Depends(get_db)],
    token_data: Annotated[
        schemas.TokenData, Depends(dependencies.get_verified_token_data)
    ],
):
    return crud.get_places(
        db,
        [
            role.division.id
            for role in token_data.roles
            if role.role_name in (schemas.Role.director, schemas.Role.manager)
        ],
    )


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
