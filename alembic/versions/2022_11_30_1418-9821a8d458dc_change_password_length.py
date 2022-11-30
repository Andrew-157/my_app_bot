"""change password length

Revision ID: 9821a8d458dc
Revises: b9c334133a97
Create Date: 2022-11-30 14:18:49.596151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9821a8d458dc'
down_revision = 'b9c334133a97'
branch_labels = None
depends_on = None


def upgrade() -> None:

    with op.batch_alter_table('Accounts') as batch_op:
        batch_op.alter_column('password',
                              existing_type=sa.String(length=50),
                              type_=sa.String(length=20),
                              existing_nullable=False)


def downgrade() -> None:

    with op.batch_alter_table('Accounts') as batch_op:
        batch_op.alter_column('password',
                              existing_type=sa.String(length=20),
                              type_=sa.String(length=50),
                              existing_nullable=False)
