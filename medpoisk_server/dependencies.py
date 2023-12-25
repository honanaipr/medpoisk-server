from .database import SessionLocal
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from . import security
from . import schemas
from . import models
from .crud import get_employee_by_username
import jwt

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
    anauthorized_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User not authorized",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        employee_data = security.jwt_decode(token)
    except jwt.exceptions.ExpiredSignatureError:
        raise anauthorized_exc
    employee = get_employee_by_username(employee_data.username, session)
    if not employee:
        raise anauthorized_exc
    return employee
