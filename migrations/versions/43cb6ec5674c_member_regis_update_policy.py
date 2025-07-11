"""Member_Regis_update_policy.

Revision ID: 43cb6ec5674c
Revises: 4747456e69c4
Create Date: 2025-06-30 15:40:18.841573

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '43cb6ec5674c'
down_revision = '4747456e69c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    \
    with op.batch_alter_table('members', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title_name_th', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('title_name_en', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('address', sa.String(length=400), nullable=True))
        batch_op.add_column(sa.Column('province', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('zip_code', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('phone_no', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('policy_accepted', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('terms_condition_accepted', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('received_news', sa.Boolean(), nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=200),
               existing_nullable=False)

    with op.batch_alter_table('service_invoices', schema=None) as batch_op:
        batch_op.alter_column('total_price',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)

    with op.batch_alter_table('service_payments', schema=None) as batch_op:
        batch_op.alter_column('amount_due',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('service_payments', schema=None) as batch_op:
        batch_op.alter_column('amount_due',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)

    with op.batch_alter_table('service_invoices', schema=None) as batch_op:
        batch_op.alter_column('total_price',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)

    with op.batch_alter_table('members', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.drop_column('received_news')
        batch_op.drop_column('terms_condition_accepted')
        batch_op.drop_column('policy_accepted')
        batch_op.drop_column('phone_no')
        batch_op.drop_column('zip_code')
        batch_op.drop_column('province')
        batch_op.drop_column('address')
        batch_op.drop_column('title_name_en')
        batch_op.drop_column('title_name_th')

    # ### end Alembic commands ###
