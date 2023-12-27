from datetime import datetime, timedelta
from typing import Annotated

from fastapi import APIRouter, Cookie, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import http_exceptions, schemas, security
from ..config import config
from ..crud import get_employee_by_username, get_roles_by_employee_id
from ..dependencies import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def get_token(
    response: Response,
    session: Annotated[Session, Depends(get_db)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    employee = get_employee_by_username(form_data.username, session)
    roles = get_roles_by_employee_id(employee.id, session)
    if not employee:
        raise http_exceptions.UnauthorizedException
    if not security.validate_password(form_data.password, employee.password_hash):
        raise http_exceptions.UnauthorizedException
    access_token_data = schemas.TokenData(
        username=employee.username,
        exp=datetime.utcnow()
        + timedelta(minutes=config.jwt_settings.access_token_lifetime_minutes),
        roles=roles,
    )
    refresh_token_data = schemas.TokenData(
        username=employee.username,
        exp=datetime.utcnow()
        + timedelta(minutes=config.jwt_settings.refresh_token_lifetime_minutes),
        roles=roles,
    )
    access_token = security.jwt_encode(payload=access_token_data.model_dump())
    refresh_token = security.jwt_encode(payload=refresh_token_data.model_dump())
    response.set_cookie("refreshToken", refresh_token, httponly=True)
    return schemas.Token(access_token=access_token)


@router.post("/refresh")
async def refresh_token(
    response: Response,
    # session: Annotated[Session, Depends(get_db)],
    refresh_token: Annotated[str | None, Cookie(alias="refreshToken")] = None,
):
    if not refresh_token:
        raise http_exceptions.UnauthorizedException
    token_data = security.jwt_decode(refresh_token)
    access_token_data = schemas.TokenData(
        username=token_data.username,
        exp=datetime.utcnow()
        + timedelta(minutes=config.jwt_settings.access_token_lifetime_minutes),
        roles=token_data.roles,
    )
    refresh_token_data = schemas.TokenData(
        username=token_data.username,
        exp=datetime.utcnow()
        + timedelta(minutes=config.jwt_settings.refresh_token_lifetime_minutes),
        roles=token_data.roles,
    )
    access_token = security.jwt_encode(payload=access_token_data.model_dump())
    refresh_token = security.jwt_encode(payload=refresh_token_data.model_dump())
    response.set_cookie("refreshToken", refresh_token, httponly=True)
    return schemas.Token(access_token=access_token)
