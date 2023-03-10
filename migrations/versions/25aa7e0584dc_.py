"""empty message

Revision ID: 25aa7e0584dc
Revises: 3e88e498d43c
Create Date: 2023-02-15 14:39:01.978451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25aa7e0584dc'
down_revision = '3e88e498d43c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
