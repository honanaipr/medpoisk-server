from fastapi import APIRouter, Depends, HTTPException
from .. import crud
from ..schemas import ProductCreate, Product, ProductPublick
from sqlalchemy import UUID
from ..dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound

router = APIRouter(
    prefix="/products",
    tags=["products"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

from .. import schemas

@router.get("/", response_model=list[ProductPublick])
async def read_detailed_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_publick_products(db, skip=skip, limit=limit)

@router.put("/", response_model=Product)
async def new_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        db_product = crud.create_product(db, product) 
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Product barcode must be unique!") from e
    db.commit()
    return db_product


