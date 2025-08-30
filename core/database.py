import os, time, logging
import psycopg2
from psycopg2 import OperationalError, InterfaceError
from contextlib import contextmanager

logger = logging.getLogger(__name__)

_CONN = None
_DSN = None

def _get_dsn():
    """Build DSN on first use, after environment variables are loaded."""
    global _DSN
    if _DSN is not None:
        return _DSN
    
    # Always build from individual components to avoid URL parsing issues
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT', '5432')
    
    # Check if required variables are present
    if not all([db_host, db_name, db_user, db_password]):
        raise ValueError(f"Missing required database environment variables. Got: HOST={db_host}, NAME={db_name}, USER={db_user}, PASSWORD={'***' if db_password else None}")
    
    _DSN = (
        f"host={db_host} "
        f"port={db_port} "
        f"dbname={db_name} "
        f"user={db_user} "
        f"password={db_password} "
        f"sslmode=require "
        f"application_name=ingester "
        f"connect_timeout=10"
    )
    
    return _DSN

def _connect():
    global _CONN
    dsn = _get_dsn()  # Get DSN when we actually need it
    print(f"Attempting to connect with DSN: {dsn[:50]}...")  # Debug line
    _CONN = psycopg2.connect(dsn)
    _CONN.autocommit = False  # explicit commits per page

def get_db_connection():
    """Return a healthy connection, reconnecting if necessary."""
    global _CONN
    if _CONN is None or _CONN.closed:
        _connect()
    return _CONN

@contextmanager
def db_cursor():
    """Cursor with commit/rollback + auto-reconnect on connection drops."""
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        yield cur
        conn.commit()
    except (OperationalError, InterfaceError) as e:
        logger.warning("DB connection dropped (%s); reconnecting…", e)
        try:
            conn.close()
        except Exception:
            pass
        _connect()
        raise
    except Exception:
        conn.rollback()
        raise
    finally:
        try:
            cur.close()
        except Exception:
            pass

def exec_many(sql, rows):
    """Helper for batch inserts (commit handled by db_cursor)."""
    with db_cursor() as cur:
        cur.executemany(sql, rows)

def exec_one(sql, params=None):
    with db_cursor() as cur:
        cur.execute(sql, params)