"""Add data de cadastro

Revision ID: 31369704d778
Revises: 
Create Date: 2023-03-29 23:01:57.623381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31369704d778'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hosts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_cad', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hosts', schema=None) as batch_op:
        batch_op.drop_column('date_cad')

    # ### end Alembic commands ###