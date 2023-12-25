from fastapi import APIRouter, Depends, status, Response, Request, Cookie
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from .. import security
from pydantic import BaseModel, Field
from ..dependencies import get_auntificated_employee, get_db
from ..crud import get_employee_by_username
from ..models.employee import Employee
from .. import schemas
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from .. import http_exceptions

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
