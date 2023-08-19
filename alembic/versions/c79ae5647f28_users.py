"""users

Revision ID: c79ae5647f28
Revises: 52f6cc1cdc07
Create Date: 2023-07-25 11:12:28.557773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c79ae5647f28'
down_revision = '52f6cc1cdc07'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('telegram', sa.String(length=50), nullable=False),
    sa.Column('telegram_id', sa.String(length=30), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('telegram'),
    sa.UniqueConstraint('telegram')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
