import bcrypt
import jwt

from . import schemas
from .config import config


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
) -> schemas.TokenData:
    decoded = jwt.decode(token.encode(), public_key, algorithms=[algorithm])
    token_data = schemas.TokenData.model_validate(decoded)
    return token_data


def jwt_update(
    token: str,
    private_key: str = config.jwt_settings.private_key_path.read_text(),
    public_key: str = config.jwt_settings.public_key_path.read_text(),
    algorithm: str = config.jwt_settings.algorithm,
) -> str:
    decoded = jwt.decode(token.encode(), public_key, algorithms=[algorithm])
    token_data = schemas.TokenData(username=decoded["username"], roles=decoded.roles)
    encoded = jwt.encode(token_data.model_dump(), private_key, algorithm=algorithm)
    return encoded


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())


def validate_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password)
