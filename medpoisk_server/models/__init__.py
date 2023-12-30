from ..database import Base
from .division_model import Division
from .doctor_model import Doctor
from .employee_model import Employee
from .inventory_model import Inventory
from .min_amount_model import MinAmount
from .picture_model import Picture
from .place_model import Place
from .position_model import Position
from .privilage_model import Privilage
from .product_model import Product
from .role_model import Role
from .room_model import Room

__all__ = [
    "Base",
    "Division",
    "Doctor",
    "Employee",
    "Inventory",
    "Place",
    "Position",
    "Privilage",
    "Product",
    "Role",
    "Room",
    "MinAmount",
    "Picture",
]
