import os, time, logging
import psycopg2
from psycopg2 import OperationalError, InterfaceError
from contextlib import contextmanager

logger = logging.getLogger(__name__)

_CONN = None
_DSN = None


def _load_db_settings():
    """Read DB_* env vars and validate."""
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT', '5432')
    db_sslmode = os.getenv('DB_SSLMODE', 'require')

    if not all([db_host, db_name, db_user, db_password]):
        raise ValueError(
            "Missing required database environment variables. "
            f"Got: HOST={db_host}, NAME={db_name}, USER={db_user}, "
            f"PASSWORD={'***' if db_password else None}"
        )

    return {
        "host": db_host,
        "name": db_name,
        "user": db_user,
        "password": db_password,
        "port": db_port,
        "sslmode": db_sslmode,
    }


def get_sqlalchemy_url() -> str:
    """
    Build a SQLAlchemy URL from the same DB_* env vars used for psycopg2.
    """
    cfg = _load_db_settings()
    return (
        f"postgresql+psycopg2://{cfg['user']}:{cfg['password']}"
        f"@{cfg['host']}:{cfg['port']}/{cfg['name']}?sslmode={cfg['sslmode']}"
    )


def _get_dsn():
    """Build DSN on first use, after environment variables are loaded."""
    global _DSN
    if _DSN is not None:
        return _DSN

    cfg = _load_db_settings()

    _DSN = (
        f"host={cfg['host']} "
        f"port={cfg['port']} "
        f"dbname={cfg['name']} "
        f"user={cfg['user']} "
        f"password={cfg['password']} "
        f"sslmode={cfg['sslmode']} "
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