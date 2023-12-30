from .auth_router import router as auth_router
from .doctor_router import router as doctor_router
from .inventory_router import router as inventory_router
from .limit_router import router as limit_router
from .picture_router import router as picture_router
from .places_router import router as places_router
from .position_router import router as position_router
from .product_router import router as product_router
from .profile_router import router as profile_router
from .room_router import router as room_router

__all__ = [
    "auth_router",
    "doctor_router",
    "inventory_router",
    "limit_router",
    "picture_router",
    "places_router",
    "position_router",
    "product_router",
    "profile_router",
    "room_router",
]
