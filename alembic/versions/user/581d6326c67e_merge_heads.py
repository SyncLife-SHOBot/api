"""Merge heads

Revision ID: 581d6326c67e
Revises: 650fe9a83512, 27a50b9ae9bb
Create Date: 2024-11-28 11:14:36.676354

"""

from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "581d6326c67e"
down_revision: Union[Sequence[str], None] = ("650fe9a83512", "27a50b9ae9bb")
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
