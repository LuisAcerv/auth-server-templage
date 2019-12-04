"""init database

Revision ID: a5dbc6ded394
Revises: 
Create Date: 2019-12-03 21:02:51.678481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5dbc6ded394'
down_revision = None
branch_labels = None
depends_on = None


"""
def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')
"""

def upgrade():
    op.execute("""
        CREATE SCHEMA core;
        
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
        
        CREATE TABLE core.applications (
            id UUID PRIMARY KEY UNIQUE DEFAULT uuid_generate_v4(),
            name text UNIQUE NOT NULL,
            created_at timestamp NOT NULL DEFAULT NOW(),
            token UUID UNIQUE,
            expires timestamp
        );

        CREATE SCHEMA platform;
        
        CREATE TABLE platform.users (
            id UUID PRIMARY KEY UNIQUE DEFAULT uuid_generate_v4(),   
            application_id UUID UNIQUE REFERENCES core.applications(id),
            password text;
        );

        CREATE EXTENSION pgcrypto;
        CREATE OR REPLACE FUNCTION signup_trg() 
        RETURNS TRIGGER AS 
        $$
            BEGIN
                IF TG_OP = 'INSERT' THEN 
                    UPDATE platform.users SET
                    password = crypt(NEW.password, gen_salt('bf', 8))
                    WHERE id = NEW.id; RETURN NEW;
                END IF;
            END;
        $$ LANGUAGE plpgsql;


        DROP TRIGGER IF EXISTS signup_trg ON platform.users;

        CREATE TRIGGER signup_trg 
        AFTER INSERT ON platform.users
            FOR EACH ROW EXECUTE PROCEDURE signup_trg();
    """)


def downgrade():
    op.execute(
        """
        DROP SCHEMA core CASCADE;
        DROP TABLE core.applications CASCADE;
        """
    )
