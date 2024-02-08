"""created PAFunctionalCompetencyIndicator table

Revision ID: 3119f3f3d1bf
Revises: 346d71d08188
Create Date: 2023-11-10 14:58:42.718431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3119f3f3d1bf'
down_revision = '346d71d08188'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pa_functional_competency_indicators',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('function_id', sa.Integer(), nullable=True),
    sa.Column('level_id', sa.Integer(), nullable=True),
    sa.Column('indicator', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['function_id'], ['pa_functional_competency.id'], ),
    sa.ForeignKeyConstraint(['level_id'], ['pa_functional_competency_levels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pa_functional_competency_indicators')
    # ### end Alembic commands ###