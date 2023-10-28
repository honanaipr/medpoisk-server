from fastapi import APIRouter, Depends, HTTPException
from ..crud import get_products, get_product_amount
from ..schemas import ProductPublick


router = APIRouter(
    prefix="/products",
    tags=["products"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

from .. import schemas

@router.get("/", response_model=list[ProductPublick])
async def read_products():
    db_products = get_products(db)
    products = []
    for db_product in db_products:
        product = schemas.ProductPublick(**db_product.__dict__, amount=get_product_amount(db, db_product.id))
        products.append(product)
    return products

from ..crud import init_products
from ..database import SessionLocal
db = SessionLocal()
init_products(db)
