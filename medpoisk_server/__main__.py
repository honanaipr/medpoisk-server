from .main import app
import uvicorn
from .config import config

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=config.port)
