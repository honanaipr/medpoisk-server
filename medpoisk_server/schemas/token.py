from datetime import datetime, timedelta

from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: str
    exp: datetime = Field(
        default_factory=lambda: datetime.utcnow() + timedelta(minutes=100)
    )
    iat: datetime = Field(default_factory=datetime.utcnow)
    iss: str = "medpoisk-server"
