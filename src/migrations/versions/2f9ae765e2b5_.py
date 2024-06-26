"""empty message

Revision ID: 2f9ae765e2b5
Revises:
Create Date: 2024-06-26 16:59:45.442166

"""
from alembic import op
import sqlalchemy as sa
from src.data.planets import dummy_data


# revision identifiers, used by Alembic.
revision = '2f9ae765e2b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    planets = op.create_table(
        'planets',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('type', sa.String(), nullable=True),
        sa.Column('mass', sa.String(), nullable=True),
        sa.Column('volume', sa.String(), nullable=True),
        sa.Column('temperature', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('image', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('id'),
        sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###

    op.bulk_insert(planets, dummy_data)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
