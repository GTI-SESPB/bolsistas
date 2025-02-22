"""empty message

Revision ID: c9d632d88fbc
Revises: 9fb8b9396c44
Create Date: 2024-03-13 02:05:47.179895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9d632d88fbc'
down_revision = '9fb8b9396c44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bolsa', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nome', sa.String(), nullable=False))

    with op.batch_alter_table('edital', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nome', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('edital', schema=None) as batch_op:
        batch_op.drop_column('nome')

    with op.batch_alter_table('bolsa', schema=None) as batch_op:
        batch_op.drop_column('nome')

    # ### end Alembic commands ###
