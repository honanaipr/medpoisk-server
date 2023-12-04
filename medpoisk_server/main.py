from fastapi import Depends, FastAPI
# from .internal import admin
from .routers import doctors, pictures, products, rooms, places, positions
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from .config import config

app = FastAPI()

origins = [
    "http://localhost:5173", #vite dev server on port 5173
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

v1.include_router(positions.router)
v1.include_router(products.router)
v1.include_router(rooms.router)
v1.include_router(doctors.router)
v1.include_router(places.router)
v1.include_router(pictures.router)

@app.get("/")
@app.get("/transit")
@app.get("/basket")
@app.get("/profile")
async def index(page: str|None=None):
    return FileResponse("../medpoisk-client/dist/index.html")

app.mount(
    "/pictures", StaticFiles(directory=config.pictures_dir, html=True), name="static"
)

app.mount(
    "/", StaticFiles(directory="../medpoisk-client/dist", html=True), name="static"
)
