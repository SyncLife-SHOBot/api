"""Add admin user seed

Revision ID: 2e71bd2e425d
Revises: 76fc5affe2dd
Create Date: 2024-11-04 17:47:33.714745

"""

from typing import Sequence, Union
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2e71bd2e425d"
down_revision: str = "76fc5affe2dd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Insertar usuario administrador
    op.execute(
        """
        INSERT INTO users (
            id, email, password, first_name, last_name,
            birth_date, phone, is_deleted, created_at, updated_at
        )
        VALUES (
            'ef5ba845-d921-48f2-80ab-7e05f9c220ca',
            'admin@example.com',
            '$2b$12$O.BO5x2ae0hspRcEpC7XGOCZl6Q6XRf3j.WFdlAJ2420Xk8uzoolu',
            'Admin',
            'User',
            '1990-01-01',
            '1234567890',
            FALSE,
            NOW(),
            NOW()
        )
        """
    )


def downgrade() -> None:
    # Eliminar usuario administrador en caso de downgrade
    op.execute("DELETE FROM users WHERE id = 'ef5ba845-d921-48f2-80ab-7e05f9c220ca'")
