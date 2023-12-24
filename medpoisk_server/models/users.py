from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects import postgresql
from .roles import Role
from ..database import Base
from typing import TYPE_CHECKING
from .. import schemas

if TYPE_CHECKING:
    from .divisions import Division
    from .privilages import Privilage
else:
    Division = "Division"
    Privilage = "Privilage"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    first_name: Mapped[str | None] = mapped_column(postgresql.TEXT)
    middle_name: Mapped[str | None] = mapped_column(postgresql.TEXT)
    last_name: Mapped[str] = mapped_column(postgresql.TEXT)
    email: Mapped[str | None] = mapped_column(postgresql.TEXT)
    password_hash: Mapped[str] = mapped_column(postgresql.BYTEA)

    privilages: Mapped[list[Privilage]] = relationship(back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, login={self.username})"
