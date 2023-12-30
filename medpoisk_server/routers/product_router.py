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
    pictures: list[UploadFile],
    title: Annotated[str, Form()],
    barcode: Annotated[int | None, Form()] = None,
    min_amount: Annotated[int | None, Form()] = None,
):
    new_product = schemas.ProductCreate(title=title, barcode=barcode)
    return crud.create_product(
        db,
        new_product,
        input_pictures=[
            (picture.file, picture.headers["content-type"]) for picture in pictures
        ],
    )


@router.delete("/")
async def get_detailed_product(id: int, db: Session = Depends(get_db)) -> bool:
    crud.delete_product(db, id)
    db.commit()
    return True
