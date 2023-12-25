from pydantic import BaseModel, ConfigDict


class EmployeePublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    email: str | None


class EmployeePublicDetailed(EmployeePublic):
    first_name: str | None
    middle_name: str | None
    last_name: str


class EmployeePrivate(EmployeePublicDetailed):
    password_hash: bytes
