from sqlalchemy import ForeignKey
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .privilages import Privilage
from ..database import Base
from typing import TYPE_CHECKING

# from .. import schemas
if TYPE_CHECKING:
    from .rooms import Room

    # from .users import Privilage
else:
    Room = "Room"
    # Privilage = "Privilage"


class Division(Base):
    __tablename__ = "divisions"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(postgresql.TEXT)
    address: Mapped[str] = mapped_column(postgresql.TEXT)
    super_division_id: Mapped[int | None] = mapped_column(ForeignKey("divisions.id"))

    privilages: Mapped[list[Privilage]] = relationship(back_populates="division")
    rooms: Mapped[list[Room]] = relationship(back_populates="division")
    super_division: Mapped["Division | None"] = relationship(remote_side=[id])
    sub_divisions: Mapped[list["Division"]] = relationship(
        back_populates="super_division"
    )
