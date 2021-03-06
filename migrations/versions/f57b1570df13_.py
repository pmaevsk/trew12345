"""empty message

Revision ID: f57b1570df13
Revises: 
Create Date: 2022-06-17 00:02:57.573015

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f57b1570df13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_form',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('form', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('my_form')
    # ### end Alembic commands ###
