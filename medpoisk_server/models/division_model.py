from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base
from .privilage_model import Privilage
from .room_model import Room

if TYPE_CHECKING:
    from .balacnce_model import Balance
    from .place_model import Place


class Division(Base):
    __tablename__ = "division"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(postgresql.TEXT)
    address: Mapped[str] = mapped_column(postgresql.TEXT)
    super_division_id: Mapped[int | None] = mapped_column(ForeignKey("division.id"))

    privilages: Mapped[list[Privilage]] = relationship(back_populates="division")
    rooms: Mapped[list[Room]] = relationship(back_populates="division")
    places: Mapped[list["Place"]] = relationship("Place", back_populates="division")
    super_division: Mapped["Division | None"] = relationship(remote_side=[id])
    sub_divisions: Mapped[list["Division"]] = relationship(
        back_populates="super_division"
    )
    balance: Mapped["Balance"] = relationship("Balance", back_populates="division")
