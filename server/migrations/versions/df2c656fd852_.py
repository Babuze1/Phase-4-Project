"""empty message

Revision ID: df2c656fd852
Revises: 
Create Date: 2023-10-04 20:42:56.142048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df2c656fd852'
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
    op.create_table('menu_items',
    sa.Column('MenuItem_ID', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(), nullable=True),
    sa.Column('Description', sa.Text(), nullable=True),
    sa.Column('Price', sa.Float(precision=2), nullable=True),
    sa.Column('Image_URL', sa.String(), nullable=True),
    sa.Column('Restaurant_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Restaurant_ID'], ['restaurants.Restaurant_ID'], ),
    sa.PrimaryKeyConstraint('MenuItem_ID')
    )
    op.create_table('restaurant_dietary_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('dietary_tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dietary_tag_id'], ['dietary_tags.DietaryTag_ID'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.Restaurant_ID'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('Review_ID', sa.Integer(), nullable=False),
    sa.Column('Rating', sa.Float(precision=5, asdecimal=2), nullable=True),
    sa.Column('Content', sa.Text(), nullable=True),
    sa.Column('Date_Created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('User_ID', sa.Integer(), nullable=True),
    sa.Column('Restaurant_ID', sa.Integer(), nullable=True),
    sa.Column('MenuItem_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['MenuItem_ID'], ['menu_items.MenuItem_ID'], ),
    sa.ForeignKeyConstraint(['Restaurant_ID'], ['restaurants.Restaurant_ID'], ),
    sa.ForeignKeyConstraint(['User_ID'], ['users.User_ID'], ),
    sa.PrimaryKeyConstraint('Review_ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('restaurant_dietary_tags')
    op.drop_table('menu_items')
    op.drop_table('restaurants')
    op.drop_table('users')
    op.drop_table('dietary_tags')
    # ### end Alembic commands ###
