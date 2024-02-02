from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic.type_adapter import TypeAdapter
from sqlalchemy.orm import Session

from . import http_exceptions, schemas, security
from .crud import get_employee_by_username, get_places
from .database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_auntificated_employee(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[Session, Depends(get_db)],
) -> schemas.EmployeePrivate | None:
    try:
        employee_data = security.jwt_decode(token)
    except jwt.exceptions.ExpiredSignatureError:
        raise http_exceptions.UnauthorizedException
    employee = get_employee_by_username(employee_data.username, session)
    if not employee:
        raise http_exceptions.UnauthorizedException
    return employee


def get_verified_token_data(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> schemas.TokenData:
    try:
        token_data = security.jwt_decode(token)
    except jwt.exceptions.ExpiredSignatureError:
        raise http_exceptions.UnauthorizedException
    return token_data


def get_auntificated_divisions(
    token_data: Annotated[schemas.TokenData, Depends(get_verified_token_data)],
) -> list[schemas.DivisionPublick]:
    return [role.division for role in token_data.roles]


def get_auntificated_places(
    divisions: Annotated[
        list[schemas.DivisionPublick], Depends(get_auntificated_divisions)
    ],
    session: Annotated[Session, Depends(get_db)],
) -> list[schemas.PlacePublick]:
    auntificated_plcaces = get_places(session, [division.id for division in divisions])
    return TypeAdapter(list[schemas.PlacePublick]).validate_python(auntificated_plcaces)
