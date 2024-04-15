"""Added odyssey table

Revision ID: 0ec70ce6bdda
Revises: 7f598182e8eb
Create Date: 2024-04-15 22:21:07.887783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ec70ce6bdda'
down_revision: Union[str, None] = '7f598182e8eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('odyssey',
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('departure', sa.String(), nullable=False),
    sa.Column('destination', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('odyssey')
    # ### end Alembic commands ###
