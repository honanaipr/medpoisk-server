import jwt
import bcrypt
from .config import config

from pydantic import BaseModel, Field
from datetime import datetime, timedelta


class TokenData(BaseModel):
    username: str
    exp: datetime = Field(
        default_factory=lambda: datetime.utcnow() + timedelta(minutes=100)
    )
    iat: datetime = Field(default_factory=datetime.utcnow)
    iss: str = "medpoisk-server"


def jwt_encode(
    payload: dict,
    private_key: str = config.jwt_settings.private_key_path.read_text(),
    algorithm: str = config.jwt_settings.algorithm,
) -> str:
    encoded = jwt.encode(payload, private_key, algorithm=algorithm)
    return encoded


def jwt_decode(
    token: str,
    public_key: str = config.jwt_settings.public_key_path.read_text(),
    algorithm: str = config.jwt_settings.algorithm,
) -> TokenData:
    decoded = jwt.decode(token.encode(), public_key, algorithms=[algorithm])
    token_data = TokenData.model_validate(decoded)
    return token_data


def jwt_update(
    token: str,
    private_key: str = config.jwt_settings.private_key_path.read_text(),
    public_key: str = config.jwt_settings.public_key_path.read_text(),
    algorithm: str = config.jwt_settings.algorithm,
) -> str:
    decoded = jwt.decode(token.encode(), public_key, algorithms=[algorithm])
    token_data = TokenData(username=decoded["username"])
    encoded = jwt.encode(token_data.model_dump(), private_key, algorithm=algorithm)
    return encoded


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())


def validate_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password)
