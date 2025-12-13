import time
from typing import Iterable, Any, Callable

from psycopg2 import OperationalError, InterfaceError
from psycopg2.extras import execute_batch as _psycopg_execute_batch

from core.logger import get_logger

logger = get_logger("db_batch")


def execute_batch_with_retry(
    cursor_cm: Callable[[], Any],
    sql: str,
    rows: Iterable[Iterable[Any]],
    max_retries: int = 3,
    sleep_seconds: float = 1.0,
) -> None:
    """Execute a batch insert/update with limited retries on connection errors.

    - ``cursor_cm`` is a contextmanager factory like ``core.database.db_cursor``.
    - Retries on ``OperationalError`` / ``InterfaceError`` (e.g. SSL connection closed).
    - On final failure, the exception is re-raised so callers can alert/fail.
    """
    attempt = 1
    while True:
        try:
            with cursor_cm() as cur:
                _psycopg_execute_batch(cur, sql, rows)
            return
        except (OperationalError, InterfaceError) as e:
            logger.warning(
                "Batch execute failed (attempt %s/%s): %s",
                attempt,
                max_retries,
                e,
            )
            if attempt >= max_retries:
                raise
            attempt += 1
            time.sleep(sleep_seconds)
