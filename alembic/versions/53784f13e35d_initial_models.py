# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Initial models
#
# Revision ID: 53784f13e35d
# Revises: fecb5e4a7be4
# Create Date: 2017-11-30 21:10:13.531156


from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53784f13e35d'
down_revision = 'fecb5e4a7be4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
                    sa.Column('file_id', sa.BIGINT(), nullable=False),
                    sa.Column('sha512_hash', sa.TEXT(), nullable=True),
                    sa.Column('sha256_hash', sa.TEXT(), nullable=True),
                    sa.Column('sha1_hash', sa.TEXT(), nullable=True),
                    sa.Column('md5_hash', sa.TEXT(), nullable=True),
                    sa.Column('size', sa.FLOAT(), nullable=True),
                    sa.Column('mime_type', sa.VARCHAR(length=40),
                              nullable=True),
                    sa.Column('submitted_by', sa.VARCHAR(length=120),
                              nullable=False),
                    sa.Column('status', sa.VARCHAR(length=20), nullable=False),
                    sa.Column('last_updated', sa.DATETIME(), nullable=False),
                    sa.Column('first_seen', sa.DATETIME(), nullable=False),
                    sa.PrimaryKeyConstraint('file_id')
                    )
    op.create_table('lookup_request',
                    sa.Column('request_id', sa.BIGINT(), nullable=False),
                    sa.Column('requested_at', sa.DATETIME(), nullable=False),
                    sa.Column('requestor', sa.VARCHAR(length=120),
                              nullable=False),
                    sa.Column('file_id', sa.BIGINT(), nullable=True),
                    sa.Column('lookup_hash', sa.TEXT(), nullable=False),
                    sa.Column('result', sa.VARCHAR(length=20), nullable=False),
                    sa.ForeignKeyConstraint(['file_id'], ['file.file_id'], ),
                    sa.PrimaryKeyConstraint('request_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lookup_request')
    op.drop_table('file')
    # ### end Alembic commands ###
