"""move data to new table

Revision ID: 5a8999867326
Revises: 9821a8d458dc
Create Date: 2022-11-30 15:20:18.827719

"""

from models import Account
from alembic import op
import sqlalchemy as sa
from session_folder.create_session import create_session
from sqlalchemy import create_engine
from sqlalchemy.sql import select, table

# revision identifiers, used by Alembic.
revision = '5a8999867326'
down_revision = '9821a8d458dc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    session = create_session(create_engine("sqlite:///accounts.db"))

    passwords = table('users_secret_data',
                      sa.Column('id', sa.Integer, primary_key=True),
                      sa.Column('password', sa.String(20), nullable=False)
                      )

    stmt = select(Account.id, Account.password)

    data = [{'id': value.id, 'password': value.password}
            for value in session.execute(stmt)]

    op.bulk_insert('users_secret_data', data)


def downgrade() -> None:
    op.drop_table('users_secret_data')
