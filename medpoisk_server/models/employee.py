from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base
from .privilage import Privilage


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    first_name: Mapped[str | None] = mapped_column(postgresql.TEXT)
    middle_name: Mapped[str | None] = mapped_column(postgresql.TEXT)
    last_name: Mapped[str] = mapped_column(postgresql.TEXT)
    email: Mapped[str | None] = mapped_column(postgresql.TEXT)
    password_hash: Mapped[str] = mapped_column(postgresql.BYTEA)

    privilages: Mapped[list[Privilage]] = relationship(back_populates="employee")

    def __repr__(self):
        return self._repr(
            username=self.username,
            first_name=self.first_name,
            middle_name=self.middle_name,
        )
