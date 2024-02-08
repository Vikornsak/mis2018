"""added active field to all models

Revision ID: e01bdc1d7972
Revises: c463120dc991
Create Date: 2024-01-05 02:58:35.009638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e01bdc1d7972'
down_revision = 'c463120dc991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('kpis', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))

    with op.batch_alter_table('strategies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))

    with op.batch_alter_table('strategy_activities', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))

    with op.batch_alter_table('strategy_tactics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))

    with op.batch_alter_table('strategy_themes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('strategy_themes', schema=None) as batch_op:
        batch_op.drop_column('active')

    with op.batch_alter_table('strategy_tactics', schema=None) as batch_op:
        batch_op.drop_column('active')

    with op.batch_alter_table('strategy_activities', schema=None) as batch_op:
        batch_op.drop_column('active')

    with op.batch_alter_table('strategies', schema=None) as batch_op:
        batch_op.drop_column('active')

    with op.batch_alter_table('kpis', schema=None) as batch_op:
        batch_op.drop_column('active')

    # ### end Alembic commands ###