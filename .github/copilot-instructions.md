# AI Coding Agent Instructions for dmt_fec_ingesters 

These guidelines are for AI assistants (e.g., GitHub Copilot Chat) working in this repository.
Focus on preserving existing patterns for database access, state tracking, and ingestion flows.

## Project Overview

- This project ingests FEC (Federal Election Commission) data into Postgres.
- Core pieces:
  - `core/`: environment loading, logging, DB access, shared utilities, state tracking, alerting.
  - `ingesters/`: API-specific ingestion scripts (candidates, committees, schedules A/B/E, totals).
  - `database/models.py`: SQLAlchemy ORM models mirroring the DB schema (tables + indexes).
  - `scripts/run_all_ingesters.py`: orchestration entry point that runs all ingesters with logging.
  - `alembic/`: schema migrations for the Postgres database.
  - `tests/`: pytest suite covering DB layer, helpers, and each ingester.

## Environment & Configuration

- Environment variables are loaded via `core.env.load_environment`:
  - Base config from `.env` if present, then `.env.<ENV_MODE>` (default `ENV_MODE=dev`).
  - Do **not** reimplement env loading; import and call `load_environment` where needed.
- Database settings come from `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_PORT`.
  - Use `core.database.get_db_connection`, `db_cursor`, and `get_sqlalchemy_url` instead of manual connection strings.
- Slack alerts use `SLACK_WEBHOOK_URL` (see `core/alerting.py`).
- FEC API access uses `FEC_API_KEY` and fixed base URLs inside each ingester module.

## Logging & Alerting Conventions

- Always create loggers via `core.logger.get_logger(name?)` instead of `logging.getLogger` directly.
  - The main pipeline uses `get_logger()` in `scripts/run_all_ingesters.py`.
- Error reporting to Slack uses `core.alerting.send_slack_alert(message: str)`.
  - Pattern: log a structured error message and then send a Slack alert with a prefixed emoji + context (see `api_candidates_new.py`, `api_schedule_a_ingester.py`).

## Database Access Patterns

- Low-level DB access uses psycopg2 via `core.database`:
  - Preferred pattern is `with db_cursor() as cur:` which handles commit/rollback and reconnect.
  - For batch inserts, use `psycopg2.extras.execute_batch` inside the cursor context.
- Do **not** open raw psycopg2 connections where `db_cursor` is sufficient.
- SQLAlchemy models in `database/models.py` are for schema and tooling; they are not used directly by ingesters today.
- When adding tables or columns:
  - Update `database/models.py` and create a matching Alembic migration under `alembic/versions/`.

## State Tracking & Checkpoints

- Generic, per-ingester state is stored via `core.state_tracker`:
  - `get_last_run(name, target="all"|id)` / `update_last_run(name, dt?, target)`.
  - `get_checkpoint`, `update_checkpoint`, `clear_checkpoint`, `get_checkpoint_started_at` for long-running paginated jobs.
- Schedule A demonstrates the full checkpoint pattern in `ingesters/api_schedule_a_ingester.py`:
  - Uses `ops.ingest_state` + `ops.ingest_checkpoints` with `target` = `"all"` or committee ID.
  - Includes CLI resume (`--resume-index`, `--resume-date`) and auto-resume from DB checkpoints.
- When adding new long-running or paginated ingesters, follow the Schedule A pattern for:
  - `last_run` handling, `DAYS_BACK` windows, and `target`-scoped state.
  - Checkpoint structure and `started_at` semantics.

## Target / Filtering Utilities

- Committee and candidate targeting lives in `core.utils`:
  - `load_committee_list()` returns a list of committee IDs from `ops.committee_targets` or `None` for "all" mode.
  - `load_candidate_list()` derives candidate IDs from active committee targets.
  - Helpers exist to manage targets (`add_committee_target`, `remove_committee_target`, `list_committee_targets`, `enable_all_committees_mode`).
- New ingesters that support subset modes should:
  - Use these helpers for committee/candidate lists instead of new targeting tables.
  - Mirror the dual-mode behavior: run for all entities when the list is `None`, else iterate over the returned IDs.
  - See `ingesters/api_candidates_new.py` (candidate list) and `ingesters/api_schedule_a_ingester.py` (committee list).

## Ingestion Patterns

- All ingesters follow a consistent structure:
  - Module-level constants: API URLs, `PAGE_SIZE`, `SLEEP_SECONDS`, and allowed field lists.
  - A core `run(...)` function (or `_run_*` helpers) that:
    - Reads `last_run` / checkpoints.
    - Builds `params` with `api_key`, pagination, and optional date or ID filters.
    - Calls `core.fetcher.fetch_with_retries(url, params)` for HTTP with backoff and status handling.
    - Normalizes JSON into ordered tuples matching a list of fields.
    - Uses `execute_batch` with `INSERT ... ON CONFLICT ... DO UPDATE` and `IS DISTINCT FROM` to avoid no-op updates.
    - Sleeps between pages using `SLEEP_SECONDS` to respect API limits.
  - A `main()` entry point that wires CLI args or targeting helpers and calls `run(...)`.
- When creating or modifying ingesters:
  - Reuse `fetch_with_retries` instead of new HTTP wrappers.
  - Follow the JSON → row tuple conversion pattern in `api_candidates_new.py` and `api_schedule_a_ingester.py`.
  - Preserve `ON CONFLICT` semantics and `last_updated` update logic (see Schedule A).

## Orchestration & Running the Pipeline

- The top-level orchestration script is `scripts/run_all_ingesters.py`:
  - Calls `load_environment()` before importing ingester modules.
  - Imports ingester modules and then calls their `main()` functions in a fixed order.
  - Wraps each call with `run_with_logging(name, func)` to log start/success/failure but continue on errors.
- Typical entry points:
  - Run full pipeline: `python -m scripts.run_all_ingesters` (ensure env and DB are configured).
  - Run a single ingester directly, e.g. `python -m ingesters.api_schedule_a_ingester --resume-index ...`.

## Testing Conventions

- Tests use pytest with heavy mocking of DB, HTTP, and Slack:
  - Project root added to `sys.path` in `tests/conftest.py` for imports.
  - DB behavior is tested via `test_database.py` using `db_cursor`, `_get_dsn`, etc.
  - Ingester tests (e.g. `tests/test_ingesters.py`) patch:
    - `fetch_with_retries`, `db_cursor`, `execute_batch`, `time.sleep`, Slack, and state tracker functions.
- When adding new behavior:
  - Mirror test patterns from `TestScheduleAIngester` and `TestCandidatesIngester` for pagination, state, and error paths.
  - Avoid making real network or DB calls inside tests; rely on mocks and fixtures.

## How AI Agents Should Work Here

- Prefer small, targeted changes that align with existing ingester and helper patterns.
- Before introducing new helpers or modules, look for existing equivalents in `core/` or `ingesters/` and extend them.
- Keep orchestration behavior consistent: new ingesters should expose a `main()` and be wired through `scripts/run_all_ingesters.py` with logging and tests in `tests/test_run_all_ingesters.py`.
- Never hardcode secrets or connection details; always use the environment-driven mechanisms already in place.
