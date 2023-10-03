"""empty message

Revision ID: b5957233cc05
Revises: 
Create Date: 2023-10-03 20:31:10.947659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5957233cc05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dietary_tags',
    sa.Column('DietaryTag_ID', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('DietaryTag_ID')
    )
    op.create_table('users',
    sa.Column('User_ID', sa.Integer(), nullable=False),
    sa.Column('Username', sa.String(), nullable=True),
    sa.Column('Email', sa.String(), nullable=True),
    sa.Column('Password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('User_ID'),
    sa.UniqueConstraint('Email')
    )
    op.create_table('restaurants',
    sa.Column('Restaurant_ID', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(), nullable=True),
    sa.Column('Location', sa.String(), nullable=True),
    sa.Column('Amenities', sa.String(), nullable=True),
    sa.Column('Description', sa.Text(), nullable=True),
    sa.Column('Owner_User_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Owner_User_ID'], ['users.User_ID'], ),
    sa.PrimaryKeyConstraint('Restaurant_ID'),
    sa.UniqueConstraint('Owner_User_ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurants')
    op.drop_table('users')
    op.drop_table('dietary_tags')
    # ### end Alembic commands ###
