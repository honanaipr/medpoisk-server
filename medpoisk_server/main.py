from fastapi import FastAPI

# from .internal import admin
from .routers import doctor, picture, places, position, product, auth, profile, room
from fastapi.middleware.cors import CORSMiddleware

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

v1 = FastAPI()
app.mount("/api/v0", v1)

v1.include_router(auth.router)
v1.include_router(profile.router)
v1.include_router(position.router)
v1.include_router(product.router)
v1.include_router(room.router)
v1.include_router(doctor.router)
v1.include_router(places.router)
v1.include_router(picture.router)
