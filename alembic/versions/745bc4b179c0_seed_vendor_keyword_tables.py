"""seed vendor keyword tables

Revision ID: 745bc4b179c0
Revises: 513d7ee58e9a
Create Date: 2025-12-11 20:12:31.436505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '745bc4b179c0'
down_revision: Union[str, Sequence[str], None] = '513d7ee58e9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # vendor_name_keywords
    op.execute("""
        INSERT INTO vendor_name_keywords (kw, category) VALUES
          ('media',      'Media & Digital Advertising'),
          ('digital',    'Media & Digital Advertising'),
          ('advert',     'Media & Digital Advertising'),
          ('market',     'Media & Digital Advertising'),
          ('payments',   'Fundraising & Direct-Response'),
          ('consult',    'Consulting & Strategy'),
          ('strateg',    'Consulting & Strategy'),
          ('print',      'Printing & Mail Production'),
          ('mailer',     'Printing & Mail Production'),
          ('sign',       'Printing & Mail Production'),
          ('poll',       'Polling & Research'),
          ('research',   'Polling & Research'),
          ('payroll',    'Payroll & Staff'),
          ('travel',     'Travel & Lodging'),
          ('legal',      'Legal & Compliance')
        ON CONFLICT (kw) DO NOTHING;
    """)

    # purpose_keywords
    op.execute("""
        INSERT INTO purpose_keywords (kw, category) VALUES
          ('fundrais',       'Fundraising & Direct-Response'),
          ('direct mail',    'Fundraising & Direct-Response'),
          ('list rental',    'Fundraising & Direct-Response'),
          ('merchant fee',   'Fundraising & Direct-Response'),
          ('processing fee', 'Fundraising & Direct-Response'),
          ('media buy',      'Media & Digital Advertising'),
          ('advert',         'Media & Digital Advertising'),
          ('market',         'Media & Digital Advertising'),
          ('print',          'Printing & Mail Production'),
          ('sign',           'Printing & Mail Production'),
          ('poll',           'Polling & Research'),
          ('survey',         'Polling & Research'),
          ('travel',         'Travel & Lodging'),
          ('hotel',          'Travel & Lodging'),
          ('transfer',       'Transfers / Contributions'),
          ('legal',          'Legal & Compliance'),
          ('filing fee',     'Legal & Compliance'),
          ('compliance',     'Legal & Compliance')
        ON CONFLICT (kw) DO NOTHING;
    """)

    # vendor_category_manual
    op.execute("""
        INSERT INTO vendor_category_manual (recipient_name, category) VALUES
          ('STRATEGIC MEDIA PLACEMENT INC.', 'Media & Digital Advertising'),
          ('BASE ENGAGER, LLC',              'Media & Digital Advertising'),
          ('The Strategy Group for Media Inc.', 'Media & Digital Advertising'),
          ('THE STRATEGY GROUP FOR MEDIA INC.', 'Media & Digital Advertising'),
          ('GUSTO',                          'Payroll & Staff')
        ON CONFLICT (recipient_name) DO NOTHING;
    """)


def downgrade() -> None:
    # Remove only the seeded rows (leave any user-added data alone)
    op.execute("""
        DELETE FROM vendor_name_keywords
        WHERE kw IN (
          'media','digital','advert','market','payments',
          'consult','strateg','print','mailer','sign',
          'poll','research','payroll','travel','legal'
        );
    """)

    op.execute("""
        DELETE FROM purpose_keywords
        WHERE kw IN (
          'fundrais','direct mail','list rental','merchant fee',
          'processing fee','media buy','advert','market','print',
          'sign','poll','survey','travel','hotel','transfer',
          'legal','filing fee','compliance'
        );
    """)

    op.execute("""
        DELETE FROM vendor_category_manual
        WHERE recipient_name IN (
          'STRATEGIC MEDIA PLACEMENT INC.',
          'BASE ENGAGER, LLC',
          'The Strategy Group for Media Inc.',
          'THE STRATEGY GROUP FOR MEDIA INC.',
          'GUSTO'
        );
    """)