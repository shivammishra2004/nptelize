"""remove unique constraint for subject teacher

Revision ID: 798619c2616c
Revises: 7dc6b0df0ee0
Create Date: 2025-05-13 16:40:56.993080

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '798619c2616c'
down_revision: Union[str, None] = '7dc6b0df0ee0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_subjects_teacher_id', 'subjects', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_subjects_teacher_id', 'subjects', ['teacher_id'])
    # ### end Alembic commands ###
