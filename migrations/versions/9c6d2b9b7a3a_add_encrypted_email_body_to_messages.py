"""add encrypted email body to messages

Revision ID: 9c6d2b9b7a3a
Revises: 6071f1eea074
Create Date: 2026-01-09 04:21:10.000000

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "9c6d2b9b7a3a"
down_revision = "6071f1eea074"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("messages", schema=None) as batch_op:
        batch_op.add_column(sa.Column("encrypted_email_body", sa.Text(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("messages", schema=None) as batch_op:
        batch_op.drop_column("encrypted_email_body")
