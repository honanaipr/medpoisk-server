from datetime import datetime, timedelta
from typing import Annotated

from fastapi import APIRouter, Cookie, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .. import http_exceptions, security
from ..crud import get_employee_by_username
from ..dependencies import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login")
async def get_token(
    response: Response,
    session: Annotated[Session, Depends(get_db)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    employee = get_employee_by_username(form_data.username, session)
    if not employee:
        raise http_exceptions.UnauthorizedException
    if not security.validate_password(form_data.password, employee.password_hash):
        raise http_exceptions.UnauthorizedException
    access_token_data = security.TokenData(
        username=employee.username, exp=datetime.utcnow() + timedelta(seconds=10)
    )
    refresh_token_data = security.TokenData(
        username=employee.username, exp=datetime.utcnow() + timedelta(minutes=5)
    )
    access_token = security.jwt_encode(payload=access_token_data.model_dump())
    refresh_token = security.jwt_encode(payload=refresh_token_data.model_dump())
    response.set_cookie("refreshToken", refresh_token, httponly=True)
    return Token(access_token=access_token)


@router.post("/refresh")
async def refresh_token(
    response: Response,
    # session: Annotated[Session, Depends(get_db)],
    refresh_token: Annotated[str | None, Cookie(alias="refreshToken")] = None,
):
    if not refresh_token:
        raise http_exceptions.UnauthorizedException
    token_data = security.jwt_decode(refresh_token)
    access_token_data = security.TokenData(
        username=token_data.username, exp=datetime.utcnow() + timedelta(seconds=30)
    )
    refresh_token_data = security.TokenData(
        username=token_data.username, exp=datetime.utcnow() + timedelta(minutes=5)
    )
    access_token = security.jwt_encode(payload=access_token_data.model_dump())
    refresh_token = security.jwt_encode(payload=refresh_token_data.model_dump())
    response.set_cookie("refreshToken", refresh_token, httponly=True)
    return Token(access_token=access_token)
