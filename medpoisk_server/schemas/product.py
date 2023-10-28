from pydantic import BaseModel, ConfigDict
from uuid import uuid4, UUID

class ProductBase(BaseModel):
    title: str
    min_amount: int
    barcode: int

class ProductCreate(ProductBase):
    pass

class ProductPublickShort(ProductBase):
    pass

class ProductPublick(ProductBase):
    amount: int

class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID