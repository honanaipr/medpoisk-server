import uvicorn

from .app import app
from .config import config


def run():
    uvicorn.run(app, host="0.0.0.0", port=config.port)
