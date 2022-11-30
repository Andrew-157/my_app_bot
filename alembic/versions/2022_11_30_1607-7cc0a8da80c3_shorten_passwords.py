"""shorten passwords

Revision ID: 7cc0a8da80c3
Revises: 5a8999867326
Create Date: 2022-11-30 16:07:31.700577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cc0a8da80c3'
down_revision = '5a8999867326'
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
