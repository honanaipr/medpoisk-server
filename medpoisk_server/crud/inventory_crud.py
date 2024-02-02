from pydantic.type_adapter import TypeAdapter
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas


def get_inventory(
    db: Session, division_ids: list[int]
) -> list[schemas.InventoryItmePublick]:
    print("hello")
    stmt = (
        select(models.Inventory)
        .join(models.Inventory.place)
        .join(models.Place.division)
        .where(models.Division.id.in_(division_ids))
    )
    return TypeAdapter(list[schemas.InventoryItmePublick]).validate_python(
        list(db.scalars(stmt)), from_attributes=True
    )


def move_inventory_item(move_request: schemas.MoveRequest, db: Session):
    stmt = (
        select(models.Inventory)
        .where(models.Inventory.place_id == move_request.from_place_id)
        .where(models.Inventory.product_id == move_request.product_id)
    )
    db_inventory_from_item = db.scalars(stmt).one()
    if db_inventory_from_item.amount - move_request.amount < 0:
        raise Exception
    elif db_inventory_from_item.amount - move_request.amount == 0:
        db.delete(db_inventory_from_item)
    else:
        db_inventory_from_item.amount -= move_request.amount

    stmt = (
        select(models.Inventory)
        .where(models.Inventory.place_id == move_request.from_place_id)
        .where(models.Inventory.product_id == move_request.product_id)
    )
    db_inventory_to_item = db.scalars(stmt).one_or_none()
    if db_inventory_to_item is not None:
        db_inventory_to_item.amount += move_request.amount
    else:
        db_inventory_to_item = models.Inventory(
            product_id=move_request.product_id,
            place_id=move_request.to_place_id,
            amount=move_request.amount,
        )
        db.add(db_inventory_to_item)

    # db_transaction = models.Transaction
    # TODO update transaction table
    # TODO update balance table
