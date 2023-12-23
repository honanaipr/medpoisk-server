from pydantic_settings import BaseSettings
from pydantic import Field, BaseModel
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent


class JWTSettings(BaseModel):
    private_key_path: Path = BASE_PATH / "scripts" / "jwt-private.pem"
    public_key_path: Path = BASE_PATH / "scripts" / "jwt-public.pem"
    algorithm: str = "RS256"


class Settings(BaseSettings):
    pictures_dir: str = Field(default="./pictures")
    sqlalchemy_db_url: str = Field(
        default="postgresql://postgres:password@localhost/medpoisk"
    )
    static_path: str = Field(default="static")
    port: int = Field(default=8000)
    jwt_settings: JWTSettings = JWTSettings()


config = Settings()
