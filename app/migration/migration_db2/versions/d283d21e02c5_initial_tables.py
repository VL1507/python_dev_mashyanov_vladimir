"""Initial tables

Revision ID: d283d21e02c5
Revises:
Create Date: 2025-03-06 18:37:47.315269

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d283d21e02c5"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "event_type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.VARCHAR(length=20), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "space_type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.VARCHAR(length=20), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "logs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("datetime", sa.DateTime(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("space_type_id", sa.Integer(), nullable=False),
        sa.Column("event_type_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["event_type_id"],
            ["event_type.id"],
        ),
        sa.ForeignKeyConstraint(
            ["space_type_id"],
            ["space_type.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("logs")
    op.drop_table("space_type")
    op.drop_table("event_type")
    # ### end Alembic commands ###
