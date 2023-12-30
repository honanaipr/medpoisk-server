from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

BASE_PATH = Path(__file__).parent.parent


class JWTSettings(BaseModel):
    private_key_path: Path = BASE_PATH / "scripts" / "jwt-private.pem"
    public_key_path: Path = BASE_PATH / "scripts" / "jwt-public.pem"
    access_token_lifetime_minutes: int = 5
    refresh_token_lifetime_minutes: int = 30
    algorithm: str = "RS256"


class Settings(BaseSettings):
    pictures_dir: Path = Field((BASE_PATH / "pictures").absolute())
    pictures_base_url: str = Field(default="pictures")
    sqlalchemy_db_url: str = Field(
        default="postgresql://postgres:password@localhost/medpoisk"
    )
    port: int = Field(default=8000)
    jwt_settings: JWTSettings = JWTSettings()


config = Settings()
