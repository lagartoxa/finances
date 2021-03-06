"""001 - Adding User model

Revision ID: c720518f1a54
Revises: 
Create Date: 2021-12-25 03:08:11.548673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c720518f1a54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_user',
    sa.Column('pk', sa.BigInteger(), nullable=False),
    sa.Column('rm_timestamp', sa.Integer(), server_default='0', nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('email', 'rm_timestamp', name='project_user_email_rm_timestamp_un'),
    sa.UniqueConstraint('login', 'rm_timestamp', name='project_user_login_rm_timestamp_un')
    )
    op.create_index(op.f('ix_project_user_email'), 'project_user', ['email'], unique=False)
    op.create_index(op.f('ix_project_user_login'), 'project_user', ['login'], unique=False)
    op.create_index(op.f('ix_project_user_name'), 'project_user', ['name'], unique=False)
    op.create_index(op.f('ix_project_user_password'), 'project_user', ['password'], unique=False)
    op.create_index(op.f('ix_project_user_pk'), 'project_user', ['pk'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_user_pk'), table_name='project_user')
    op.drop_index(op.f('ix_project_user_password'), table_name='project_user')
    op.drop_index(op.f('ix_project_user_name'), table_name='project_user')
    op.drop_index(op.f('ix_project_user_login'), table_name='project_user')
    op.drop_index(op.f('ix_project_user_email'), table_name='project_user')
    op.drop_table('project_user')
    # ### end Alembic commands ###
