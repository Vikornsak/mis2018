"""added new is_expired column in Process table

Revision ID: 24989b8f2b54
Revises: 1636ce6ef639
Create Date: 2024-11-06 10:21:03.487979

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '24989b8f2b54'
down_revision = '1636ce6ef639'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('db_processes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_expired', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('db_processes', schema=None) as batch_op:
        batch_op.drop_column('is_expired')

    # ### end Alembic commands ###