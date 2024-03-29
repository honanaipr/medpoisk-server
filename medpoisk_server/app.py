from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import (
    auth_router,
    doctor_router,
    inventory_router,
    limit_router,
    picture_router,
    places_router,
    product_router,
    profile_router,
    room_router,
    transaction_router,
)

app = FastAPI()

origins = [
    "http://localhost:5173",  # vite dev server on port 5173
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

v0 = FastAPI()
app.mount("/api/v0", v0)

v0.include_router(auth_router)
v0.include_router(profile_router)
v0.include_router(product_router)
v0.include_router(room_router)
v0.include_router(doctor_router)
v0.include_router(places_router)
v0.include_router(picture_router)
v0.include_router(inventory_router)
v0.include_router(limit_router)
v0.include_router(transaction_router)
