from typing import List, Optional
from core.database import db_cursor
import logging

logger = logging.getLogger()

def load_committee_list() -> Optional[List[str]]:
    """
    Load committee IDs from the database.
    Returns None for "all committees" mode, or a list of specific committee IDs.
    """
    try:
        with db_cursor() as cur:
            cur.execute("""
                SELECT committee_id 
                FROM ops.committee_targets 
                WHERE active = TRUE 
                AND committee_id IS NOT NULL
                ORDER BY committee_id
            """)
            
            rows = cur.fetchall()
            if not rows:
                logger.info("No active committee targets found, running for ALL committees")
                return None
            
            # Filter out any None values just in case
            committee_ids = [row[0] for row in rows if row[0] is not None]
            
            if not committee_ids:
                logger.info("No valid committee targets found, running for ALL committees")
                return None
                
            logger.info(f"Loaded {len(committee_ids)} committee targets: {committee_ids}")
            return committee_ids
            
    except Exception as e:
        logger.error(f"Error loading committee targets from database: {e}")
        logger.info("Falling back to ALL committees mode")
        return None

def add_committee_target(committee_id: str, committee_name: str = None, description: str = None) -> bool:
    """Add a new committee target to the database."""
    try:
        with db_cursor() as cur:
            cur.execute("""
                INSERT INTO ops.committee_targets (committee_id, committee_name, description)
                VALUES (%s, %s, %s)
                ON CONFLICT (committee_id) DO UPDATE SET
                    committee_name = COALESCE(EXCLUDED.committee_name, ops.committee_targets.committee_name),
                    description = COALESCE(EXCLUDED.description, ops.committee_targets.description),
                    active = TRUE,
                    updated_at = NOW()
            """, (committee_id, committee_name, description))
            
            logger.info(f"Added/updated committee target: {committee_id}")
            return True
            
    except Exception as e:
        logger.error(f"Error adding committee target {committee_id}: {e}")
        return False

def remove_committee_target(committee_id: str) -> bool:
    """Deactivate a committee target."""
    try:
        with db_cursor() as cur:
            cur.execute("""
                UPDATE ops.committee_targets 
                SET active = FALSE, updated_at = NOW()
                WHERE committee_id = %s
            """, (committee_id,))
            
            if cur.rowcount > 0:
                logger.info(f"Deactivated committee target: {committee_id}")
                return True
            else:
                logger.warning(f"Committee target not found: {committee_id}")
                return False
                
    except Exception as e:
        logger.error(f"Error removing committee target {committee_id}: {e}")
        return False

def list_committee_targets() -> List[dict]:
    """List all committee targets (active and inactive)."""
    try:
        with db_cursor() as cur:
            cur.execute("""
                SELECT committee_id, committee_name, description, active, created_at, updated_at
                FROM ops.committee_targets 
                ORDER BY active DESC, committee_id
            """)
            
            columns = ['committee_id', 'committee_name', 'description', 'active', 'created_at', 'updated_at']
            return [dict(zip(columns, row)) for row in cur.fetchall()]
            
    except Exception as e:
        logger.error(f"Error listing committee targets: {e}")
        return []

def enable_all_committees_mode() -> bool:
    """Deactivate all committee targets to enable 'all committees' mode."""
    try:
        with db_cursor() as cur:
            cur.execute("""
                UPDATE ops.committee_targets 
                SET active = FALSE, updated_at = NOW()
                WHERE active = TRUE
            """)
            
            logger.info(f"Deactivated {cur.rowcount} committee targets - enabled ALL committees mode")
            return True
            
    except Exception as e:
        logger.error(f"Error enabling all committees mode: {e}")
        return False
