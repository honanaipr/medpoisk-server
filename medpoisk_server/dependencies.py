from .database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from . import security
from . import schemas
from .crud import get_employee_by_username
import jwt
from . import http_exceptions

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
