"""empty message

Revision ID: 720ad8b4711a
Revises: 915d27de520b
Create Date: 2023-12-22 06:15:34.436945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "720ad8b4711a"
down_revision: Union[str, None] = "915d27de520b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "divisions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.TEXT(), nullable=False),
        sa.Column("address", sa.TEXT(), nullable=False),
        sa.Column("super_division", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["super_division"],
            ["divisions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("first_name", sa.TEXT(), nullable=True),
        sa.Column("middle_name", sa.TEXT(), nullable=True),
        sa.Column("last_name", sa.TEXT(), nullable=False),
        sa.Column("email", sa.TEXT(), nullable=True),
        sa.Column("password_hash", sa.TEXT(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "privilages",
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("division_id", sa.Integer(), nullable=True),
        sa.Column(
            "role_id",
            postgresql.ENUM(
                "doctor",
                "manager",
                "director",
                name="ROLE",
            ),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["division_id"],
            ["divisions.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("privilages")
    op.drop_table("users")
    op.drop_table("divisions")
    # ### end Alembic commands ###
