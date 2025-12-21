# dmt_fec_ingesters

Ingests Federal Election Commission (FEC) data from the OpenFEC API into PostgreSQL.

This repo is designed to run as:
- a one-off container (local Docker) for manual runs, or
- a scheduled, one-off Fly.io machine for daily ingestion.

## What it does

- Fetches data from the OpenFEC API with retry/backoff handling.
- Upserts into Postgres tables using batched inserts.
- Tracks incremental progress using DB-backed state and checkpoints.
- Optionally sends Slack alerts on failures.

## Repo layout

- `core/`: env loading, logging, DB access, HTTP fetcher, state tracking, targeting utilities, Slack alerting.
- `ingesters/`: one module per OpenFEC endpoint/data set.
- `database/`: SQLAlchemy metadata for Alembic + schema representation.
- `alembic/`: schema migrations.
- `scripts/run_all_ingesters.py`: orchestration entrypoint that runs all ingesters.
- `tests/`: pytest suite.

## Prerequisites

- Python (repo uses a virtualenv locally; Docker image uses Python 3.11).
- Postgres 16+ recommended.
- An OpenFEC API key.
- (Optional) A Slack Incoming Webhook URL for alerts.

## Configuration

Configuration is environment-driven. Environment files are loaded by `core.env.load_environment()` in this order:
1) `.env` (if present)
2) `.env.<ENV_MODE>` (defaults to `.env.dev` when `ENV_MODE` is not set)

### Minimum `.env` config

This is the smallest practical config for running the pipeline locally (venv or Docker):

```dotenv
# Required
FEC_API_KEY=...

# Required (unless you provide DATABASE_URL instead)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=campaign_finance
DB_USER=postgres
DB_PASSWORD=postgres

# Recommended for local Docker Postgres (no TLS by default)
DB_SSLMODE=disable

# Optional
# SLACK_WEBHOOK_URL=...
```

### Required

- `FEC_API_KEY`: OpenFEC API key.
  - How to get a key: see the OpenFEC developer docs at https://api.open.fec.gov/developers/
- Database connection (choose one):
  - `DATABASE_URL` (full SQLAlchemy URL), or
  - `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, optional `DB_PORT`.

### Optional

- `ENV_MODE`: defaults to `dev`.
- `SLACK_WEBHOOK_URL`: enables Slack alerts.
  - This project uses a Slack Incoming Webhook URL (not a Slack OAuth token).
  - Create/configure an Incoming Webhook here: https://api.slack.com/messaging/webhooks
- `DB_SSLMODE`: defaults to `require`.
  - For local Docker Postgres (no TLS by default), set `DB_SSLMODE=disable`.

## Local development (venv)

Create and activate a venv, install deps, run tests:

- Create venv: `python -m venv .venv`
- Activate (PowerShell): `.\.venv\Scripts\Activate.ps1`
- Install: `pip install -r requirements.txt`
- Tests: `pytest -q`

Run all ingesters locally (requires DB + API key):

- `python -m scripts.run_all_ingesters`

## Running tests

From your activated venv:

- Run all tests: `pytest`
- Quieter output: `pytest -q`

If you’re running inside Docker, run tests in the `ingester` container image (one-off):

- `docker compose run --rm ingester pytest -q`

Note: tests mock network/DB in most cases, but some tests may assume DB env vars are present.

## Logging to file

Set `LOG_TO_FILE=True` (case-insensitive) to enable file logging.

- Logs write to `logs/ingestion.log`
- Log file rotates at ~5MB and keeps up to 5 backups

Example (dotenv):

```dotenv
LOG_TO_FILE=True
```

## Local run (Docker Compose)

`docker-compose.yml` provides:
- `db`: Postgres 16
- `ingester`: builds this repo and runs migrations + the ingestion pipeline once

Typical workflow:

1) Set env vars (at minimum `FEC_API_KEY`).
2) Start:
   - `docker compose up --build`

Notes:
- The container entrypoint runs `alembic upgrade head` and then `python -m scripts.run_all_ingesters`.
- If you connect to the compose Postgres from your host Python (not from the container), ensure your env points to `localhost:5432` and set `DB_SSLMODE=disable`.

## Database migrations (Alembic)

Apply migrations:

- `alembic upgrade head`

Create a new migration:

- `alembic revision -m "your message" --autogenerate`

Alembic configuration:
- `alembic/env.py` loads env vars and will use `DATABASE_URL` if present; otherwise it builds the URL from `DB_*` settings.
- Autogenerate is configured to compare types and server defaults.

## How ingestion works

### Orchestration

The main orchestrator is `python -m scripts.run_all_ingesters`. It:
- loads env first
- runs each ingester in a fixed order
- logs start/success/failure per ingester and continues even if one fails

### Ingesters

Each ingester typically:
- builds request params including `api_key`, pagination, and optional filters
- calls `core.fetcher.fetch_with_retries(url, params)`
- converts JSON rows into tuples matching a fixed field list
- executes batched upserts (`INSERT ... ON CONFLICT ... DO UPDATE`) using `psycopg2.extras.execute_batch`
- sleeps briefly between pages to respect API limits

### Incremental state and checkpoints

Progress is tracked in the DB (schema: `ingest`):
- `ingest.ingest_state`: stores a `last_run` timestamp per ingester and optional `target`
- `ingest.ingest_checkpoints`: stores checkpoint payloads (pagination/index/date), plus `started_at` to support resuming long jobs

Some ingesters support two modes:
- **All mode**: processes all committees/candidates and uses checkpoints for resumability.
- **Targeted mode**: processes a subset of committees/candidates based on `ops.committee_targets`.

#### Targeted ingestion prerequisite (external table)

Targeted ingestion requires a table named `ops.committee_targets`.

This repo intentionally does **not** create or migrate the `ops` schema or `ops.committee_targets` table; it’s managed in a separate repo.

At minimum, targeted mode expects:
- `ops.committee_targets.committee_id`
- `ops.committee_targets.active` (boolean)

Targeting utilities live in `core.utils`.

## Running a single ingester

Most ingesters can be executed as modules, for example:

- `python -m ingesters.api_schedule_a_ingester`

Some support resume CLI flags (see the module’s `main()`), e.g. resume index/date for long runs.

## Deployment and scheduled runs (Fly.io + GitHub Actions)

- `.github/workflows/deploy.yml` builds the Fly image on pushes to `main` (build-only).
- `.github/workflows/run_ingesters.yml` runs on a daily cron schedule and:
  - starts a one-off Fly machine using the latest image
  - runs `/app/docker-entrypoint.sh` (migrations + ingestion)
  - streams logs
  - destroys the machine
  - posts to Slack on failure (if configured)

Fly app configuration is in `fly.toml`. Secrets are expected to be set via `fly secrets set`.

## Troubleshooting

- **Local Postgres + SSL**: the code defaults to `sslmode=require`. For local Docker Postgres, set `DB_SSLMODE=disable`.
- **Missing env**: most failures early in startup are missing `FEC_API_KEY` or DB settings.
- **Rate limits**: OpenFEC can return 429; retries/backoff are handled in `core.fetcher`.

## Security and data handling

- Do not commit secrets. Use `.env` files locally and `fly secrets` in production.
- Treat ingested data as operational data; apply your organization’s retention and access policies.
