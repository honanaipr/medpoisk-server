from sqlalchemy import ForeignKey
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base
from .privilage import Privilage
from .room import Room


class Division(Base):
    __tablename__ = "division"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(postgresql.TEXT)
    address: Mapped[str] = mapped_column(postgresql.TEXT)
    super_division_id: Mapped[int | None] = mapped_column(ForeignKey("division.id"))

    privilages: Mapped[list[Privilage]] = relationship(back_populates="division")
    rooms: Mapped[list[Room]] = relationship(back_populates="division")
    super_division: Mapped["Division | None"] = relationship(remote_side=[id])
    sub_division: Mapped[list["Division"]] = relationship(
        back_populates="super_division"
    )
