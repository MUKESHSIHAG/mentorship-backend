"""users table

Revision ID: c16276194ba9
Revises: 40c6ceced9ee
Create Date: 2020-03-02 21:43:50.495636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c16276194ba9'
down_revision = '40c6ceced9ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('available_to_mentor', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('bio', sa.String(length=500), nullable=True))
    op.add_column('user', sa.Column('interests', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('location', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('need_mentoring', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('occupation', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('organization', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('photo_url', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('resume_url', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('skills', sa.String(length=500), nullable=True))
    op.add_column('user', sa.Column('slack_username', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('social_media_links', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'social_media_links')
    op.drop_column('user', 'slack_username')
    op.drop_column('user', 'skills')
    op.drop_column('user', 'resume_url')
    op.drop_column('user', 'photo_url')
    op.drop_column('user', 'organization')
    op.drop_column('user', 'occupation')
    op.drop_column('user', 'need_mentoring')
    op.drop_column('user', 'location')
    op.drop_column('user', 'interests')
    op.drop_column('user', 'bio')
    op.drop_column('user', 'available_to_mentor')
    # ### end Alembic commands ###
