from fastapi import APIRouter, Depends, HTTPException, status, Response, Request, Cookie
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from .. import security
from pydantic import BaseModel, Field
from ..dependencies import get_auntificated_user, get_db
from ..crud import get_user_by_username
from ..models.users import User
from .. import schemas
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth", tags=["auth"])

unauthorized_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="User not authorized",
    headers={"WWW-Authenticate": "Bearer"},
)


@router.get("/profile", response_model=schemas.UserPublicDetailed)
async def send_profile_data(
    user: Annotated[User | None, Depends(get_auntificated_user)]
):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return user


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login")
async def get_token(
    response: Response,
    session: Annotated[Session, Depends(get_db)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    user = get_user_by_username(form_data.username, session)
    if not user:
        raise unauthorized_exc
    if not security.validate_password(form_data.password, user.password_hash):
        raise unauthorized_exc
    access_token_data = security.TokenData(
        username=user.username, exp=datetime.utcnow() + timedelta(seconds=10)
    )
    refresh_token_data = security.TokenData(
        username=user.username, exp=datetime.utcnow() + timedelta(minutes=5)
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
        raise unauthorized_exc
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
