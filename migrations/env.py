# alembic/env.py

from alembic import context
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from api import create_app  # Adjust this import based on your project structure
from config import DevelopmentConfig  # Adjust this import based on your project structure
from models.base_model import Base  # Adjust this import based on your project structure


app = create_app(config_class=DevelopmentConfig)
db = app.extensions['sqlalchemy'].db  # Adjust based on how you initialize SQLAlchemy in your app

# Load target metadata from your SQLAlchemy models
target_metadata = Base.metadata

# Alembic configuration
config = context.config
config.set_main_option('sqlalchemy.url', app.config['SQLALCHEMY_DATABASE_URI'])

# Other Alembic configurations as needed

def run_migrations_online():
    engine = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )
    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        process_revision_directives=True,
    )
    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

# Check if Alembic is running in offline mode
if context.is_offline_mode():
    # Handle offline migrations
    # Example:
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()
else:
    # Run migrations online
    run_migrations_online()
