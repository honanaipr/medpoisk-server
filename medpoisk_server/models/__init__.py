from ..database import Base
from .division import Division
from .doctor import Doctor
from .employee import Employee
from .inventory import Inventory
from .min_amount import MinAmount
from .picture import Picture
from .place import Place
from .position import Position
from .privilage import Privilage
from .product import Product
from .role import Role
from .room import Room

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
