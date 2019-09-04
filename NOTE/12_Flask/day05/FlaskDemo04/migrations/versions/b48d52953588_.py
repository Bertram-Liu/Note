"""empty message

Revision ID: b48d52953588
Revises: b38a2277bae2
Create Date: 2019-05-07 16:36:18.851776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b48d52953588'
down_revision = 'b38a2277bae2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('cid', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'teacher', 'course', ['cid'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teacher', type_='foreignkey')
    op.drop_column('teacher', 'cid')
    # ### end Alembic commands ###