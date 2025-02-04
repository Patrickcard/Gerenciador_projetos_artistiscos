"""Adicionando campos de orçamento e cronograma ao Projeto

Revision ID: 23ec93ccc8b6
Revises: 
Create Date: 2024-07-13 12:22:30.502406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23ec93ccc8b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('budget', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('timeline', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_column('timeline')
        batch_op.drop_column('budget')

    # ### end Alembic commands ###
