from pydantic import BaseModel, ConfigDict

from .place import Place


class ProductBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    # min_amount: int
    barcode: int


class ProductCreate(ProductBase):
    pass


class ProductPublick(ProductBase):
    id: int
    amount: int
    places: list[Place]
    picture_url: str | None


class ProductShortPublick(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
