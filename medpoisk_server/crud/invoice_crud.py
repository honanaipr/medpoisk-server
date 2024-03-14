from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas


def create_invoice(db: Session, invoice: schemas.Invoice) -> models.Invoice:
    db_invoice = models.Invoice(**invoice.model_dump())
    db.add(db_invoice)


def read_invoices(db: Session) -> Iterable[models.Invoice]:
    stmt = select(models.Invoice)
    db_invoices = db.scalars(stmt)
    return db_invoices


def read_invoice(db: Session, invoice_id: int) -> models.Invoice:
    stmt = select(models.Invoice).where(models.Invoice.id == invoice_id)
    db_invoice = db.scalar(stmt)
    return db_invoice
