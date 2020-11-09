"""added leave quota id and year column in StaffLeaveRemainQuota table

Revision ID: f36790081696
Revises: c906f4fa0b89
Create Date: 2020-06-24 09:32:37.918703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f36790081696'
down_revision = 'c906f4fa0b89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('staff_leave_remain_quota', sa.Column('leave_quota_id', sa.Integer(), nullable=True))
    op.add_column('staff_leave_remain_quota', sa.Column('year', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'staff_leave_remain_quota', 'staff_leave_quota', ['leave_quota_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'staff_leave_remain_quota', type_='foreignkey')
    op.drop_column('staff_leave_remain_quota', 'year')
    op.drop_column('staff_leave_remain_quota', 'leave_quota_id')
    # ### end Alembic commands ###