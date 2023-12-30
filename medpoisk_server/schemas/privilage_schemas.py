from pydantic import BaseModel, ConfigDict

from .division_schemas import DivisionPrivate
from .role_schemas import Role


class PrivilagePrivate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    division: DivisionPrivate
    role_name: Role
