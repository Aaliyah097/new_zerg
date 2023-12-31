"""wallets

Revision ID: ea9d27268d01
Revises: 1ea973e4f095
Create Date: 2023-07-25 12:06:15.741538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea9d27268d01'
down_revision = '1ea973e4f095'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wallets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=50), nullable=False),
    sa.Column('currency', sa.String(length=30), nullable=False),
    sa.Column('balance', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.telegram'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallets')
    # ### end Alembic commands ###
