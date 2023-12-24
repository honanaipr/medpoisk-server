"""rename role_id column

Revision ID: 198c96ee4983
Revises: 71bf33f1c8b6
Create Date: 2023-12-24 04:18:26.384666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "198c96ee4983"
down_revision: Union[str, None] = "71bf33f1c8b6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("privilages", "role_id", new_column_name="role_name")


def downgrade() -> None:
    op.alter_column("privilages", "role_name", new_column_name="role_id")
