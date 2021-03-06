"""empty message

Revision ID: 9474aeb50a2c
Revises: e71e95b8304c
Create Date: 2022-01-05 17:55:46.622802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9474aeb50a2c'
down_revision = 'e71e95b8304c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('asset', sa.Column('added_by', sa.String(length=64), nullable=True))
    op.create_foreign_key(None, 'asset', 'user', ['added_by'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'asset', type_='foreignkey')
    op.drop_column('asset', 'added_by')
    # ### end Alembic commands ###
