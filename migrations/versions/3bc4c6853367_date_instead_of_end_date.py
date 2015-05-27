"""date instead of end_date

Revision ID: 3bc4c6853367
Revises: 2f12902f7f55
Create Date: 2015-05-26 13:15:57.630974

"""

# revision identifiers, used by Alembic.
revision = '3bc4c6853367'
down_revision = '2f12902f7f55'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_constraint('unq_name_per_project_per_day', 'flakyteststat')
    op.drop_index('idx_flakyteststat_end_date', 'flakyteststat')
    op.execute('ALTER TABLE flakyteststat RENAME COLUMN end_date TO date')
    op.execute('UPDATE flakyteststat SET date=date-1')
    op.create_index('idx_flakyteststat_date', 'flakyteststat', ['date'])
    op.create_unique_constraint('unq_name_per_project_per_day', 'flakyteststat', ['name', 'project_id', 'date'])


def downgrade():
    op.drop_constraint('unq_name_per_project_per_day', 'flakyteststat')
    op.drop_index('idx_flakyteststat_date', 'flakyteststat')
    op.execute('ALTER TABLE flakyteststat RENAME COLUMN date TO end_date')
    op.execute('UPDATE flakyteststat SET end_date=end_date+1')
    op.create_index('idx_flakyteststat_end_date', 'flakyteststat', ['end_date'])
    op.create_unique_constraint('unq_name_per_project_per_day', 'flakyteststat', ['name', 'project_id', 'end_date'])
