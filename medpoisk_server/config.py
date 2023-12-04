from pydantic_settings import BaseSettings
from pydantic import Field


class Config(BaseSettings):
    pictures_dir:str = Field("../pictures/")
    sqlalchemy_db_url:str = Field("postgresql://postgres:password@localhost/medpoisk")
    port:int = Field(80)
config = Config()