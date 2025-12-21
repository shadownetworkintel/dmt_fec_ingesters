from typing import Optional, Dict, Any
from datetime import datetime
from psycopg2.extras import Json
from core.database import db_cursor
import logging

logger = logging.getLogger(__name__)

def get_last_run(name: str, target: str = "all") -> Optional[str]:
    logger.info(f"Getting last run for: {name}, target: {target}")
    with db_cursor() as cur:
        cur.execute("select last_run from ingest.ingest_state where name=%s and target=%s", (name, target))
        row = cur.fetchone()
        result = row[0].isoformat() if row and row[0] else None
        logger.info(f"Last run for {name}/{target}: {result}")
        return result

def update_last_run(name: str, dt: Optional[datetime] = None, target: str = "all") -> None:
    logger.info(f"Updating last run for: {name}, target: {target}, dt: {dt}")
    with db_cursor() as cur:
        cur.execute("""
            insert into ingest.ingest_state(name, target, last_run, updated_at)
            values (%s, %s, COALESCE(%s, now()), now())
            on conflict (name, target) do update
              set last_run = EXCLUDED.last_run,
                  updated_at = now()
        """, (name, target, dt))
        logger.info(f"Successfully updated last run for {name}/{target}")

def get_checkpoint(name: str, target: str = "all") -> Optional[Dict[str, Any]]:
    logger.info(f"Getting checkpoint for: {name}, target: {target}")
    with db_cursor() as cur:
        cur.execute("select data from ingest.ingest_checkpoints where name=%s and target=%s", (name, target))
        row = cur.fetchone()
        result = row[0] if row else None
        logger.info(f"Checkpoint for {name}/{target}: {result}")
        return result

def update_checkpoint(name: str, checkpoint_data: Dict[str, Any], target: str = "all", started_at: Optional[datetime] = None) -> None:
    # Add started_at to the checkpoint data
    if started_at:
        checkpoint_data = checkpoint_data.copy()  # Don't modify the original
        checkpoint_data["started_at"] = started_at.isoformat()
    
    logger.info(f"Updating checkpoint for: {name}, target: {target}, data: {checkpoint_data}")
    with db_cursor() as cur:
        cur.execute("""
            insert into ingest.ingest_checkpoints(name, target, data, updated_at)
            values (%s, %s, %s, now())
            on conflict (name, target) do update
              set data = EXCLUDED.data,
                  updated_at = now()
        """, (name, target, Json(checkpoint_data)))
        logger.info(f"Successfully updated checkpoint for {name}/{target}")

def clear_checkpoint(name: str, target: str = "all") -> None:
    logger.info(f"Clearing checkpoint for: {name}, target: {target}")
    with db_cursor() as cur:
        cur.execute("delete from ingest.ingest_checkpoints where name=%s and target=%s", (name, target))
        rows_deleted = cur.rowcount
        logger.info(f"Cleared checkpoint for {name}/{target}, rows deleted: {rows_deleted}")

def get_checkpoint_started_at(name: str, target: str = "all") -> Optional[datetime]:
    """Get the started_at timestamp from a checkpoint, if it exists."""
    checkpoint = get_checkpoint(name, target)
    if checkpoint and "started_at" in checkpoint:
        try:
            return datetime.fromisoformat(checkpoint["started_at"])
        except (ValueError, TypeError) as e:
            logger.warning(f"Invalid started_at in checkpoint for {name}/{target}: {e}")
    return None