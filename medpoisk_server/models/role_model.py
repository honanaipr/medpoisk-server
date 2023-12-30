from sqlalchemy.dialects import postgresql

from ..database import Base

Role = postgresql.ENUM(
    "doctor", "manager", "director", name="ROLE", metadata=Base.metadata
)
