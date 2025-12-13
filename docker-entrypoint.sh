#!/usr/bin/env sh
set -e

# Run Alembic migrations against the configured database
alembic upgrade head

# Run the full ingestion pipeline
python -m scripts.run_all_ingesters

# Keep container alive so Fly doesn’t restart it
sleep infinity