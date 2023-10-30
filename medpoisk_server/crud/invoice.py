from .. import schemas, models
from sqlalchemy import update

# def process_add_invoice(positions: list[schemas.PositionCreate]):
#     for position in positions:
#         update(models.Position).where(models.Product.id == position.product.id).values(amount -= position.ampunt)