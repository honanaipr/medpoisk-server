from fastapi import Depends, FastAPI
from .internal import admin
from .routers import items, doctors, rooms, places
from fastapi.staticfiles import StaticFiles

app = FastAPI()

v1 = FastAPI()
app.mount("/api/v0", v1)

v1.include_router(items.router)
v1.include_router(rooms.router)
v1.include_router(doctors.router)
v1.include_router(places.router)

app.mount(
    "/", StaticFiles(directory="../medpoisk-client/dist", html=True), name="static"
)
