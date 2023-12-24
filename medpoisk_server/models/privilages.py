from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects import postgresql
from .roles import Role
from ..database import Base
from typing import TYPE_CHECKING
from .. import schemas

if TYPE_CHECKING:
    from .users import User
    from .divisions import Division
else:
    User = "User"
    Division = "Division"


class Privilage(Base):
    __tablename__ = "privilages"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    division_id: Mapped[int] = mapped_column(ForeignKey("divisions.id"))
    role_name: Mapped[str] = mapped_column(Role)

    user: Mapped[User] = relationship(back_populates="privilages")
    division: Mapped[Division] = relationship(back_populates="privilages")
