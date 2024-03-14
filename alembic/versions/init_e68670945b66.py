"""init

Revision ID: e68670945b66
Revises:
Create Date: 2024-03-03 18:19:58.096959

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e68670945b66"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "division",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.TEXT(), nullable=False),
        sa.Column("address", sa.TEXT(), nullable=False),
        sa.Column("super_division_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["super_division_id"],
            ["division.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "doctor",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "employee",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("first_name", sa.TEXT(), nullable=True),
        sa.Column("middle_name", sa.TEXT(), nullable=True),
        sa.Column("last_name", sa.TEXT(), nullable=False),
        sa.Column("email", sa.TEXT(), nullable=True),
        sa.Column("password_hash", postgresql.BYTEA(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "invoice",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("barcode", sa.BigInteger(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    op.create_table(
        "balance",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("division_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("avg_price", postgresql.MONEY(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["division_id"],
            ["division.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "limit",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("division_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("min_amount", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["division_id"],
            ["division.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "picture",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("url", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "place",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("division_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["division_id"],
            ["division.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "privilage",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("employee_id", sa.Integer(), nullable=False),
        sa.Column("division_id", sa.Integer(), nullable=False),
        sa.Column("role_name", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["division_id"],
            ["division.id"],
        ),
        sa.ForeignKeyConstraint(
            ["employee_id"],
            ["employee.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "room",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("division_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["division_id"],
            ["division.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "inventory",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("place_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["place_id"],
            ["place.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "transaction",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("invoice_id", sa.Integer(), nullable=True),
        sa.Column("from_place_id", sa.Integer(), nullable=True),
        sa.Column("to_place_id", sa.Integer(), nullable=True),
        sa.Column("room_id", sa.Integer(), nullable=True),
        sa.Column("employee_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Numeric(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["employee_id"],
            ["employee.id"],
        ),
        sa.ForeignKeyConstraint(
            ["from_place_id"],
            ["place.id"],
        ),
        sa.ForeignKeyConstraint(
            ["invoice_id"],
            ["invoice.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.ForeignKeyConstraint(
            ["room_id"],
            ["place.id"],
        ),
        sa.ForeignKeyConstraint(
            ["to_place_id"],
            ["place.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("transaction")
    op.drop_table("inventory")
    op.drop_table("room")
    op.drop_table("privilage")
    op.drop_table("place")
    op.drop_table("picture")
    op.drop_table("limit")
    op.drop_table("balance")
    op.drop_table("product")
    op.drop_table("invoice")
    op.drop_table("employee")
    op.drop_table("doctor")
    op.drop_table("division")
    # ### end Alembic commands ###