from fastapi import Depends, FastAPI
from .internal import admin
from .routers import items, doctors, rooms, places
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(items.router, prefix="/api/v0")
app.include_router(rooms.router, prefix="/api/v0")
app.include_router(doctors.router, prefix="/api/v0")
app.include_router(places.router, prefix="/api/v0")

app.mount(
    "/", StaticFiles(directory="../medpoisk-client/dist", html=True), name="static"
)
