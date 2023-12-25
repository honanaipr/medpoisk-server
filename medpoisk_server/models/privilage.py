from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects import postgresql
from .role import Role
from ..database import Base
from typing import TYPE_CHECKING
from .. import schemas

if TYPE_CHECKING:
    from .employee import Employee
    from .division import Division
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
