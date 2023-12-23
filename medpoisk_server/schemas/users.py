from pydantic import BaseModel, ConfigDict


class UserPublic(BaseModel):
    username: str
    email: str | None

    model_config = ConfigDict(from_attributes=True)


class UserPublicDetailed(UserPublic):
    first_name: str | None
    middle_name: str | None
    last_name: str


class UserPrivate(UserPublicDetailed):
    password_hash: str
