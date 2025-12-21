"""drop committee_run_state

Revision ID: 3e878947a502
Revises: 895c1a422122
Create Date: 2025-12-20 20:02:11.707748

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e878947a502'
down_revision: Union[str, Sequence[str], None] = '895c1a422122'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("DROP TABLE IF EXISTS ingest.committee_run_state")


def downgrade() -> None:
    """Downgrade schema."""
    op.create_table(
        "committee_run_state",
        sa.Column("schedule_name", sa.Text(), nullable=False),
        sa.Column("committee_id", sa.Text(), nullable=False),
        sa.Column("last_run", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("schedule_name", "committee_id"),
        schema="ingest",
    )
