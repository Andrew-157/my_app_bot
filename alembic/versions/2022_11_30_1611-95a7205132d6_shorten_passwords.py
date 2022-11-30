"""shorten passwords

Revision ID: 95a7205132d6
Revises: 9821a8d458dc
Create Date: 2022-11-30 16:11:00.260343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95a7205132d6'
down_revision = '9821a8d458dc'
branch_labels = None
depends_on = None


def upgrade() -> None:

    with op.batch_alter_table('Accounts') as batch_op:
        batch_op.alter_column('password',
                              existing_type=sa.String(length=20),
                              type_=sa.String(length=4),
                              existing_nullable=False)


def downgrade() -> None:

    with op.batch_alter_table('Accounts') as batch_op:
        batch_op.alter_column('password',
                              existing_type=sa.String(length=4),
                              type_=sa.String(length=20),
                              existing_nullable=False)
