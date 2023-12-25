from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from . import http_exceptions, schemas, security
from .crud import get_employee_by_username
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
