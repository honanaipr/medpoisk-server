from pydantic.type_adapter import TypeAdapter
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas


def get_inventory(
    db: Session, token_data: schemas.TokenData
) -> list[schemas.InventoryItmePublick]:
    print("hello")
    stmt = (
        select(models.Inventory)
        .join(models.Inventory.place)
        .join(models.Place.division)
        .where(models.Division.id.in_([role.division.id for role in token_data.roles]))
    )
    return TypeAdapter(list[schemas.InventoryItmePublick]).validate_python(
        list(db.scalars(stmt)), from_attributes=True
    )
