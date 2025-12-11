from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from core.env import load_environment
from core.database import get_sqlalchemy_url

# Load env vars (DB_* etc.)
load_environment()

# Alembic Config
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import your models' Base
from database.models import Base

target_metadata = Base.metadata


def get_url() -> str:
    """Resolve the database URL for Alembic."""
    # 1) Allow explicit DATABASE_URL override if set
    url = os.getenv("DATABASE_URL")
    if url:
        return url

    # 2) Otherwise, use the same DB_* config as core.database
    return get_sqlalchemy_url()


# Make sure alembic.ini sees the same URL (helps for 'alembic revision --autogenerate')
config.set_main_option("sqlalchemy.url", get_url())

def include_object(object, name, type_, reflected, compare_to):
    """Only include objects in the 'fec' schema."""
    if type_ == "table":
        # Only process tables in 'fec' schema
        if hasattr(object, "schema"):
            return object.schema == "fec"
        return False

    # For indexes, FKs, etc., check parent table's schema
    if hasattr(object, "table") and hasattr(object.table, "schema"):
        return object.table.schema == "fec"

    # Default: include
    return True


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_schemas=True,
        include_object=include_object,
        version_table_schema="fec",  # store alembic_version in fec schema
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        # 1. Ensure 'fec' schema exists in its own committed transaction
        with connection.begin():
            connection.exec_driver_sql("CREATE SCHEMA IF NOT EXISTS fec")

        # 2. Configure Alembic to use fec.alembic_version
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            include_object=include_object,
            version_table_schema="fec",
            compare_type=True,
            compare_server_default=True,
        )

        # 3. Run migrations in Alembic's transaction
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
