from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base
from .role import Role

if TYPE_CHECKING:
    from .division import Division
    from .employee import Employee
else:
    Employee = "Employee"
    Division = "Division"


class Privilage(Base):
    __tablename__ = "privilage"

    id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    division_id: Mapped[int] = mapped_column(ForeignKey("division.id"))
    role_name: Mapped[str] = mapped_column(Role)

    employee: Mapped[Employee] = relationship(back_populates="privilages")
    division: Mapped[Division] = relationship(back_populates="privilage")
