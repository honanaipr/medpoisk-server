from pydantic import BaseModel, ConfigDict

from .picture import PicturePublick


class ProductBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    # min_amount: int
    barcode: int


class ProductCreate(ProductBase):
    pass


class ProductPublick(ProductBase):
    id: int
    title: str
    barcode: int
    description: str
    pictures: list[PicturePublick]


class ProductShortPublick(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
