from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    pictures_dir:str = Field("./pictures")
    sqlalchemy_db_url:str = Field("postgresql://postgres:password@localhost/medpoisk")
    static_path:str = Field("static")
    port:int = Field(80)

config = Settings()