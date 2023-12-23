from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects import postgresql
from .roles import Role
from ..database import Base


privilages_table = Table(
    "privilages",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("division_id", ForeignKey("divisions.id")),
    Column("role_id", Role),
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    first_name: Mapped[str | None] = mapped_column(postgresql.TEXT)
    middle_name: Mapped[str | None] = mapped_column(postgresql.TEXT)
    last_name: Mapped[str] = mapped_column(postgresql.TEXT)
    email: Mapped[str | None] = mapped_column(postgresql.TEXT)
    password_hash: Mapped[str] = mapped_column(postgresql.TEXT)

    def __repr__(self):
        return f"User(id={self.id}, login={self.login})"
