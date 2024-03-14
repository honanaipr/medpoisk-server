from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

if TYPE_CHECKING:
    from .division_model import Division
    from .employee_model import Employee


class Privilage(Base):
    __tablename__ = "privilage"

    id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    division_id: Mapped[int] = mapped_column(ForeignKey("division.id"))
    role_name: Mapped[str]

    employee: Mapped["Employee"] = relationship("Employee", back_populates="privilages")
    division: Mapped["Division"] = relationship("Division", back_populates="privilages")
