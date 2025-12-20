"""add ingest schema tables

Revision ID: 8c1f0a2b3d4e
Revises: 11aac41aa8fa
Create Date: 2025-12-19

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "8c1f0a2b3d4e"
down_revision: Union[str, Sequence[str], None] = "11aac41aa8fa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS ingest")

    op.create_table(
        "ingest_state",
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column(
            "target",
            sa.String(length=50),
            server_default=sa.text("'all'"),
            nullable=False,
        ),
        sa.Column("last_run", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=True),
        sa.PrimaryKeyConstraint("name", "target"),
        schema="ingest",
    )
    op.create_index(
        "idx_ingest_state_name_target",
        "ingest_state",
        ["name", "target"],
        unique=False,
        schema="ingest",
    )

    op.create_table(
        "ingest_checkpoints",
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column(
            "target",
            sa.String(length=50),
            server_default=sa.text("'all'"),
            nullable=False,
        ),
        sa.Column(
            "data",
            postgresql.JSONB(astext_type=sa.Text()),
            server_default=sa.text("'{}'::jsonb"),
            nullable=False,
        ),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=True),
        sa.PrimaryKeyConstraint("name", "target"),
        schema="ingest",
    )
    op.create_index(
        "idx_ingest_checkpoints_name_target",
        "ingest_checkpoints",
        ["name", "target"],
        unique=False,
        schema="ingest",
    )

    op.create_table(
        "committee_run_state",
        sa.Column("schedule_name", sa.Text(), nullable=False),
        sa.Column("committee_id", sa.Text(), nullable=False),
        sa.Column("last_run", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=True),
        sa.PrimaryKeyConstraint("schedule_name", "committee_id"),
        schema="ingest",
    )


def downgrade() -> None:
    op.drop_table("committee_run_state", schema="ingest")
    op.drop_index("idx_ingest_checkpoints_name_target", table_name="ingest_checkpoints", schema="ingest")
    op.drop_table("ingest_checkpoints", schema="ingest")
    op.drop_index("idx_ingest_state_name_target", table_name="ingest_state", schema="ingest")
    op.drop_table("ingest_state", schema="ingest")

    # Drop schema only if empty
    op.execute("DROP SCHEMA IF EXISTS ingest")
