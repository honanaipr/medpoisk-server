from pydantic_settings import BaseSettings
from pydantic import Field, BaseModel
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent


class JWTSettings(BaseModel):
    private_key_path: Path = BASE_PATH / "scripts" / "jwt-private.pem"
    public_key_path: Path = BASE_PATH / "scripts" / "jwt-public.pem"
    algorithm: str = "RS256"


class Settings(BaseSettings):
    pictures_dir: str = Field("./pictures")
    sqlalchemy_db_url: str = Field("postgresql://postgres:password@localhost/medpoisk")
    static_path: str = Field("static")
    port: int = Field(8000)
    jwt_settings: JWTSettings = JWTSettings()


config = Settings()
