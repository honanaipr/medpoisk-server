from sqlalchemy import ForeignKey
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import mapped_column, Mapped

from ..database import Base


class Division(Base):
    __tablename__ = "divisions"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(postgresql.TEXT)
    address: Mapped[str] = mapped_column(postgresql.TEXT)
    super_division: Mapped[int | None] = mapped_column(ForeignKey("divisions.id"))
