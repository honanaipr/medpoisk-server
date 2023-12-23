from sqlalchemy.orm import Session
from .. import schemas
from .. import models
from sqlalchemy import select, exists


def get_user_by_username(username: str, session: Session) -> schemas.UserPrivate | None:
    stmt = select(models.User).where(models.User.username == username)
    db_user = session.scalar(stmt)
    if not db_user:
        return None
    return schemas.UserPrivate.model_validate(db_user)
