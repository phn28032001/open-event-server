"""empty message

Revision ID: 70941b60bc7d
Revises: d469443aed74
Create Date: 2016-08-09 00:16:08.668419

"""

# revision identifiers, used by Alembic.
revision = '70941b60bc7d'
down_revision = 'd469443aed74'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'closing_datetime')
    op.drop_column('events_version', 'closing_datetime')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events_version', sa.Column('closing_datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('events', sa.Column('closing_datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
