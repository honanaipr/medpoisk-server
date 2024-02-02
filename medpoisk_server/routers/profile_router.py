from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, dependencies, http_exceptions, schemas

router = APIRouter(
    prefix="/profile",
    tags=["profile"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/me", response_model=schemas.EmployeePublicDetailed)
async def get_profile_data(
    employee: Annotated[
        schemas.EmployeePrivate, Depends(dependencies.get_auntificated_employee)
    ],
):
    return employee


@router.get("/staff")
async def get_staff(
    token_data: Annotated[
        schemas.TokenData, Depends(dependencies.get_verified_token_data)
    ],
    session: Annotated[Session, Depends(dependencies.get_db)],
    division_id: int | None = None,
    role_name: schemas.Role | None = None,
):
    if division_id:
        if division_id not in [
            role.division.id
            for role in token_data.roles
            if role.role_name in (schemas.Role.director, schemas.Role.manager)
        ]:
            raise http_exceptions.UnauthorizedException
        division_ids = [division_id]
    else:
        division_ids = [
            role.division.id
            for role in token_data.roles
            if role.role_name != schemas.Role.doctor
        ]
    employees = crud.get_staff(session, division_ids, role_name)

    return employees
