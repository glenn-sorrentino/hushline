"""add message encrypted email body

Revision ID: c9bafdd8f4e1
Revises: b6a1e3f5a2b1
Create Date: 2025-03-04 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "c9bafdd8f4e1"
down_revision = "b6a1e3f5a2b1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("messages", schema=None) as batch_op:
        batch_op.add_column(sa.Column("encrypted_email_body", sa.Text(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("messages", schema=None) as batch_op:
        batch_op.drop_column("encrypted_email_body")
