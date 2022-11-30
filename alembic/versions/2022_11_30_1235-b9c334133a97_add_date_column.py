"""add date column

Revision ID: b9c334133a97
Revises: 9fb08ea2e7e0
Create Date: 2022-11-30 12:35:29.568624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9c334133a97'
down_revision = '9fb08ea2e7e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'Accounts', sa.Column('created_at', sa.Date(),
                              default=sa.func.current_date())
    )


def downgrade() -> None:
    op.drop_column('Accounts', 'created_at')
