"""Added ServiceCustomerContact model

Revision ID: 320a206ed17b
Revises: a8e76ab682e9
Create Date: 2024-11-13 15:43:37.208606

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '320a206ed17b'
down_revision = 'a8e76ab682e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service_customer_contacts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('adder_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adder_id'], ['service_customer_infos.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['service_customer_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service_customer_contacts')
    # ### end Alembic commands ###