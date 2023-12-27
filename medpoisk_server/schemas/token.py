from datetime import datetime, timedelta

from pydantic import BaseModel, ConfigDict, Field

from .division import DivisionPublick
from .role import Role


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class RoleInDivision(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    division: DivisionPublick
    role_name: Role


class TokenData(BaseModel):
    username: str
    roles: list[RoleInDivision]
    exp: datetime = Field(
        default_factory=lambda: datetime.utcnow() + timedelta(minutes=100)
    )
    iat: datetime = Field(default_factory=datetime.utcnow)
    iss: str = "medpoisk-server"
