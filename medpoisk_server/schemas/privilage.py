from pydantic import BaseModel, ConfigDict

from .division import DivisionPrivate
from .role import Role


class PrivilagePrivate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    division: DivisionPrivate
    role_name: Role
