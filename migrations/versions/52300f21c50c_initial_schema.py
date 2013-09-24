"""Initial schema

Revision ID: 52300f21c50c
Revises: None
Create Date: 2013-09-23 17:04:46.177950

"""

# revision identifiers, used by Alembic.
revision = '52300f21c50c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('repository',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('node',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('label', sa.String(length=128), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('author',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('remoteentity',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('type', sa.Enum(), nullable=False),
    sa.Column('provider', sa.String(length=128), nullable=False),
    sa.Column('remote_id', sa.String(length=128), nullable=False),
    sa.Column('internal_id', sa.GUID(), nullable=False),
    sa.Column('data', sa.JSONEncodedDict(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('internal_id'),
    sa.UniqueConstraint('provider','remote_id','type', name='remote_identifier')
    )
    op.create_table('revision',
    sa.Column('repository_id', sa.GUID(), nullable=False),
    sa.Column('sha', sa.String(length=40), nullable=False),
    sa.Column('author_id', sa.GUID(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['repository_id'], ['repository.id'], ),
    sa.PrimaryKeyConstraint('repository_id', 'sha')
    )
    op.create_table('project',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('slug', sa.String(length=64), nullable=False),
    sa.Column('repository_id', sa.GUID(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['repository_id'], ['repository.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('patch',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('repository_id', sa.GUID(), nullable=False),
    sa.Column('project_id', sa.GUID(), nullable=False),
    sa.Column('parent_revision_sha', sa.String(length=40), nullable=False),
    sa.Column('label', sa.String(length=64), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.Column('diff', sa.LargeBinary(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['repository_id'], ['repository.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('build',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('repository_id', sa.GUID(), nullable=False),
    sa.Column('project_id', sa.GUID(), nullable=False),
    sa.Column('parent_revision_sha', sa.String(length=40), nullable=False),
    sa.Column('patch_id', sa.GUID(), nullable=True),
    sa.Column('label', sa.String(length=64), nullable=False),
    sa.Column('status', sa.Enum(), nullable=False),
    sa.Column('result', sa.Enum(), nullable=False),
    sa.Column('date_started', sa.DateTime(), nullable=True),
    sa.Column('date_finished', sa.DateTime(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['patch_id'], ['patch.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['repository_id', 'parent_revision_sha'], ['revision.repository_id', 'revision.sha'], ),
    sa.ForeignKeyConstraint(['repository_id'], ['repository.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('filecoverage',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('build_id', sa.GUID(), nullable=False),
    sa.Column('filename', sa.String(length=256), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Text(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['build_id'], ['build.id'], ),
    sa.PrimaryKeyConstraint('id', 'filename')
    )
    op.create_table('phase',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('build_id', sa.GUID(), nullable=False),
    sa.Column('repository_id', sa.GUID(), nullable=False),
    sa.Column('project_id', sa.GUID(), nullable=False),
    sa.Column('label', sa.String(length=128), nullable=False),
    sa.Column('status', sa.Enum(), nullable=False),
    sa.Column('result', sa.Enum(), nullable=False),
    sa.Column('date_started', sa.DateTime(), nullable=True),
    sa.Column('date_finished', sa.DateTime(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['build_id'], ['build.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['repository_id'], ['repository.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('build_id', sa.GUID(), nullable=False),
    sa.Column('project_id', sa.GUID(), nullable=False),
    sa.Column('label', sa.String(length=256), nullable=False),
    sa.Column('result', sa.Enum(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['build_id'], ['build.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id', 'label')
    )
    op.create_table('step',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('build_id', sa.GUID(), nullable=False),
    sa.Column('phase_id', sa.GUID(), nullable=False),
    sa.Column('repository_id', sa.GUID(), nullable=False),
    sa.Column('project_id', sa.GUID(), nullable=False),
    sa.Column('label', sa.String(length=128), nullable=False),
    sa.Column('status', sa.Enum(), nullable=False),
    sa.Column('result', sa.Enum(), nullable=False),
    sa.Column('node_id', sa.GUID(), nullable=True),
    sa.Column('date_started', sa.DateTime(), nullable=True),
    sa.Column('date_finished', sa.DateTime(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['build_id'], ['build.id'], ),
    sa.ForeignKeyConstraint(['node_id'], ['node.id'], ),
    sa.ForeignKeyConstraint(['phase_id'], ['phase.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['repository_id'], ['repository.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('step')
    op.drop_table('test')
    op.drop_table('phase')
    op.drop_table('filecoverage')
    op.drop_table('build')
    op.drop_table('patch')
    op.drop_table('project')
    op.drop_table('revision')
    op.drop_table('remoteentity')
    op.drop_table('author')
    op.drop_table('node')
    op.drop_table('repository')
    ### end Alembic commands ###
