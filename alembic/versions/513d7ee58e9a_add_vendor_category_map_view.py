"""add vendor_category_map view

Revision ID: 513d7ee58e9a
Revises: 2b667d303573
Create Date: 2025-12-11 20:12:22.394245

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '513d7ee58e9a'
down_revision: Union[str, Sequence[str], None] = '2b667d303573'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Ensure pg_trgm extension exists
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")

    # Create / replace the view
    op.execute("""
    CREATE OR REPLACE VIEW vendor_category_map AS
    WITH all_vendors AS (
        SELECT DISTINCT recipient_name
        FROM   schedule_b_disbursements
    ),
    name_cat AS (
        SELECT av.recipient_name,
               MIN(vnk.category) AS name_category
        FROM   all_vendors av
        JOIN   vendor_name_keywords vnk
          ON   LOWER(av.recipient_name) LIKE '%'||vnk.kw||'%'
        GROUP  BY av.recipient_name
    ),
    purpose_cat AS (
        SELECT sb.recipient_name,
               MIN(pk.category) AS purpose_category
        FROM   schedule_b_disbursements sb
        JOIN   purpose_keywords pk
          ON   LOWER(sb.disbursement_description) LIKE '%'||pk.kw||'%'
        GROUP  BY sb.recipient_name
    )
    SELECT
        av.recipient_name,
        COALESCE(
            vcm_manual.category,
            pc.purpose_category,
            nc.name_category,
            'Other'
        ) AS category
    FROM   all_vendors                av
    LEFT   JOIN vendor_category_manual vcm_manual USING (recipient_name)
    LEFT   JOIN name_cat              nc          USING (recipient_name)
    LEFT   JOIN purpose_cat           pc          USING (recipient_name);
    """)


def downgrade() -> None:
    op.execute("DROP VIEW IF EXISTS vendor_category_map;")