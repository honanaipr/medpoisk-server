from typing import Annotated

from fastapi import APIRouter, Depends, Form, UploadFile
from sqlalchemy.orm import Session

from .. import crud, dependencies, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/product",
    tags=["product"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[schemas.ProductPublick])
async def get_products(db: Session = Depends(get_db)):
    return crud.get_all_products(db)


@router.put("/", response_model=schemas.ProductPublick)
async def new_product(
    db: Annotated[Session, Depends(get_db)],
    token_data: Annotated[
        schemas.TokenData, Depends(dependencies.get_verified_token_data)
    ],
    title: Annotated[str, Form()],
    pictures: list[UploadFile] = [],
    barcode: Annotated[int | None, Form()] = None,
    min_amount: Annotated[int | None, Form()] = None,
):
    new_product = schemas.ProductCreate(title=title, barcode=barcode)
    created_product = crud.create_product(
        db,
        new_product,
        input_pictures=[
            (picture.file, picture.headers["content-type"]) for picture in pictures
        ],
    )
    db.commit()
    return created_product


@router.delete("/")
async def delete_product(id: int, db: Session = Depends(get_db)) -> int:
    crud.delete_product(db, id)
    db.commit()
    return id
