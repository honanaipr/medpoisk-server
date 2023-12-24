from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .divisions import Division
else:
    Division = "Division"


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    division_id: Mapped[int] = mapped_column(
        ForeignKey("divisions.id"), onupdate="CASCADE"
    )

    division: Mapped[Division] = relationship(back_populates="rooms")
