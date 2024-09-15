"""add content column to posts table

Revision ID: 578b503ad6e3
Revises: 0581f19df364
Create Date: 2024-09-14 21:12:33.315499

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '578b503ad6e3'
down_revision: Union[str, None] = '0581f19df364'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
