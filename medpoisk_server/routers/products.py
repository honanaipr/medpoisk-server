from fastapi import APIRouter, Depends, HTTPException
from ..crud import get_products, get_product_amount, create_product
from ..schemas import ProductPublickShort, ProductCreate, Product, ProductPublick
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

@router.get("/", response_model=list[ProductPublickShort])
async def read_products(db: Session = Depends(get_db)):
    db_products = get_products(db)
    products = []
    for db_product in db_products:
        product = schemas.ProductPublickShort(**db_product.__dict__)
        products.append(product)
    return products

@router.get("/detailed", response_model=list[ProductPublick])
async def read_detailed_products(db: Session = Depends(get_db)):
    db_products = get_products(db)
    products = []
    for db_product in db_products:
        product = schemas.ProductPublick(**db_product.__dict__, amount=get_product_amount(db, db_product.id))
        products.append(product)
    return products

@router.put("/", response_model=Product)
async def new_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        return create_product(db, product)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Product barcode must be unique!") from e


from ..crud import init_products
from ..database import SessionLocal
db = SessionLocal()
init_products(db)
