from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas


def create_transaction(
    db: Session, transaction: schemas.Transaction
) -> models.Transaction:
    db_transaction = models.Transaction(**transaction.model_dump())
    db.add(db_transaction)


def read_transactions(db: Session) -> Iterable[models.Transaction]:
    stmt = select(models.Transaction)
    db_transactions = db.scalars(stmt)
    return db_transactions


def read_transaction(db: Session, transaction_id: int) -> models.Transaction:
    stmt = select(models.Transaction).where(models.Transaction.id == transaction_id)
    db_transaction = db.scalar(stmt)
    return db_transaction
