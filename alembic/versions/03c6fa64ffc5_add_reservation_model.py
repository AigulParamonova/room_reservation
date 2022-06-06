"""Add Reservation model

Revision ID: 03c6fa64ffc5
Revises: c6f830e80caf
Create Date: 2022-05-18 19:16:18.486022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03c6fa64ffc5'
down_revision = 'c6f830e80caf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'reservation',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('from_reserve', sa.DateTime(), nullable=True),
        sa.Column('to_reserve', sa.DateTime(), nullable=True),
        sa.Column('meetingroom_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['meetingroom_id'], ['meetingroom.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    # ### end Alembic commands ###
