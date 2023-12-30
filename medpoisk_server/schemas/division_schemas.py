from pydantic import BaseModel, ConfigDict


class DivisionPublick(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str


class DivisionPrivate(DivisionPublick):
    address: str
    super_division: "DivisionPrivate"
