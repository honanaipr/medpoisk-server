from fastapi import APIRouter, Depends, HTTPException
from .. import crud
from ..schemas import ProductCreate, Product, ProductPublick
from ..dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import uuid

router = APIRouter(
    prefix="/product",
    tags=["product"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[ProductPublick])
async def read_detailed_products(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_publick_products(db, skip=skip, limit=limit)


@router.put("/", response_model=Product)
async def new_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        db_product = crud.create_product(db, product)
    except IntegrityError as e:
        raise HTTPException(
            status_code=400, detail="Product barcode must be unique!"
        ) from e
    db.commit()
    return db_product


@router.delete("/{id}")
async def read_detailed_products(id: uuid.UUID, db: Session = Depends(get_db)) -> bool:
    crud.delete_products(db, id)
    db.commit()
    return True
