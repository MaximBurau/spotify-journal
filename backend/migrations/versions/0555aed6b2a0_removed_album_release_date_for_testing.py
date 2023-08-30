"""removed album release date for testing

Revision ID: 0555aed6b2a0
Revises: f8649227d33e
Create Date: 2023-08-30 22:25:17.028745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0555aed6b2a0'
down_revision = 'f8649227d33e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('album', schema=None) as batch_op:
        batch_op.drop_column('release_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('album', schema=None) as batch_op:
        batch_op.add_column(sa.Column('release_date', sa.DATE(), nullable=False))

    # ### end Alembic commands ###
