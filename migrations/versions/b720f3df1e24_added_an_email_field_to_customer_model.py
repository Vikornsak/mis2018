"""added an email field to Customer model

Revision ID: b720f3df1e24
Revises: 54b1839e9917
Create Date: 2020-08-19 20:03:54.787502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b720f3df1e24'
down_revision = '54b1839e9917'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comhealth_customers', sa.Column('email', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comhealth_customers', 'email')
    # ### end Alembic commands ###