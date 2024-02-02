from pydantic import BaseModel, ConfigDict

from .picture_schemas import PicturePublick


class ProductBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    barcode: int | None = None


class ProductCreate(ProductBase):
    pass


class ProductPublick(ProductBase):
    id: int
    title: str
    barcode: int | None
    description: str | None
    pictures: list[PicturePublick]


class ProductShortPublick(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str


class ProductIdPublick(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
