from typing import Annotated

from fastapi import APIRouter, Depends

from .. import dependencies, schemas

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


@router.get("/staff", response_model=list[schemas.EmployeePublicDetailed])
async def get_staff(
    employee: Annotated[
        schemas.EmployeePrivate, Depends(dependencies.get_auntificated_employee)
    ],
    division_id: int | None = None,
):
    # if division_id:

    return [employee]
