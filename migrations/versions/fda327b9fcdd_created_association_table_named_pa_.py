"""created association table named pa_round_employment_assoc for collect relationship of pa_round and employment in pa_rounds table

Revision ID: fda327b9fcdd
Revises: a2fdb02cb417
Create Date: 2023-07-11 10:12:26.061846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fda327b9fcdd'
down_revision = 'a2fdb02cb417'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pa_round_employment_assoc',
    sa.Column('pa_round_id', sa.Integer(), nullable=True),
    sa.Column('employment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employment_id'], ['staff_employments.id'], ),
    sa.ForeignKeyConstraint(['pa_round_id'], ['pa_rounds.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pa_round_employment_assoc')
    # ### end Alembic commands ###