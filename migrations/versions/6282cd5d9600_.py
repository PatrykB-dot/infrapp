"""empty message

Revision ID: 6282cd5d9600
Revises: 41d0e83ecda7
Create Date: 2022-01-06 21:26:10.334514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6282cd5d9600'
down_revision = '41d0e83ecda7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'asset', 'user', ['added_by'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'asset', type_='foreignkey')
    # ### end Alembic commands ###
