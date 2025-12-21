# tests/test_database.py
import pytest
from unittest.mock import patch, MagicMock, call
import psycopg2
from psycopg2 import OperationalError, InterfaceError, DatabaseError
from core.database import _get_dsn, get_db_connection, db_cursor, exec_many, exec_one
import os

class TestGetDsn:
    
    @patch.dict('os.environ', {
        'DB_HOST': 'localhost',
        'DB_NAME': 'campaign_finance',
        'DB_USER': 'testuser',
        'DB_PASSWORD': 'testpass',
        'DB_PORT': '5432'
    })
    def test_get_dsn_success(self):
        """Test successful DSN creation with all environment variables."""
        # Reset the global DSN to force rebuild
        import core.database
        core.database._DSN = None
        
        dsn = _get_dsn()
        
        expected_parts = [
            "host=localhost",
            "port=5432",
            "dbname=campaign_finance",
            "user=testuser",
            "password=testpass",
            "sslmode=require",
            "application_name=ingester",
            "connect_timeout=10"
        ]
        
        for part in expected_parts:
            assert part in dsn

    @patch.dict('os.environ', {
        'DB_HOST': 'localhost',
        'DB_NAME': 'campaign_finance',
        'DB_USER': 'testuser',
        'DB_PASSWORD': 'testpass'
        # No DB_PORT - should default to 5432
    })
    def test_get_dsn_default_port(self):
        """Test DSN creation with default port."""
        import core.database
        core.database._DSN = None
        
        dsn = _get_dsn()
        
        assert "port=5432" in dsn

    @patch.dict('os.environ', {
        'DB_HOST': 'localhost',
        'DB_NAME': 'campaign_finance',
        'DB_USER': 'testuser'
        # Missing DB_PASSWORD
    })
    def test_get_dsn_missing_password(self):
        """Test DSN creation with missing password."""
        import core.database
        core.database._DSN = None
        
        with pytest.raises(ValueError, match="Missing required database environment variables"):
            _get_dsn()

    @patch.dict('os.environ', {
        'DB_NAME': 'campaign_finance',
        'DB_USER': 'testuser',
        'DB_PASSWORD': 'testpass'
        # Missing DB_HOST
    })
    def test_get_dsn_missing_host(self):
        """Test DSN creation with missing host."""
        import core.database
        core.database._DSN = None
        
        with pytest.raises(ValueError, match="Missing required database environment variables"):
            _get_dsn()

    @patch.dict('os.environ', {}, clear=True)
    def test_get_dsn_all_missing(self):
        """Test DSN creation with all variables missing."""
        import core.database
        core.database._DSN = None
        
        with pytest.raises(ValueError, match="Missing required database environment variables"):
            _get_dsn()

    @patch.dict('os.environ', {
        'DB_HOST': 'localhost',
        'DB_NAME': 'campaign_finance',
        'DB_USER': 'testuser',
        'DB_PASSWORD': 'testpass',
        'DB_PORT': '5433'  # Custom port
    })
    def test_get_dsn_custom_port(self):
        """Test DSN creation with custom port."""
        import core.database
        core.database._DSN = None
        
        dsn = _get_dsn()
        
        assert "port=5433" in dsn

    def test_get_dsn_cached(self):
        """Test that DSN is cached after first call."""
        import core.database
        core.database._DSN = "cached_dsn_value"
        
        dsn = _get_dsn()
        
        assert dsn == "cached_dsn_value"

    @patch.dict('os.environ', {
        'DB_HOST': 'localhost',
        'DB_NAME': 'campaign_finance',
        'DB_USER': 'testuser',
        'DB_PASSWORD': 'testpass',
        'DB_PORT': '5432',
        'DB_SSLMODE': 'disable'
    })
    def test_get_dsn_respects_sslmode_env(self):
        """Test DSN creation respects DB_SSLMODE."""
        import core.database
        core.database._DSN = None

        dsn = _get_dsn()
        assert "sslmode=disable" in dsn

class TestConnect:
    
    @patch('core.database._get_dsn')
    @patch('core.database.psycopg2.connect')
    def test_connect_success(self, mock_connect, mock_get_dsn):
        """Test successful database connection."""
        mock_get_dsn.return_value = "host=localhost dbname=test"
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        
        # Import and call _connect
        from core.database import _connect
        _connect()
        
        mock_connect.assert_called_once_with("host=localhost dbname=test")
        assert mock_conn.autocommit is False

    @patch('core.database._get_dsn')
    @patch('core.database.psycopg2.connect')
    def test_connect_failure(self, mock_connect, mock_get_dsn):
        """Test connection failure."""
        mock_get_dsn.return_value = "host=localhost dbname=test"
        mock_connect.side_effect = OperationalError("Connection failed")
        
        from core.database import _connect
        
        with pytest.raises(OperationalError, match="Connection failed"):
            _connect()

class TestGetDbConnection:
    
    @patch('core.database._connect')
    def test_get_db_connection_first_time(self, mock_connect):
        """Test getting connection for the first time."""
        import core.database
        core.database._CONN = None
        
        mock_conn = MagicMock()
        mock_conn.closed = 0  # Open connection
        mock_connect.side_effect = lambda: setattr(core.database, '_CONN', mock_conn)
        
        result = get_db_connection()
        
        mock_connect.assert_called_once()
        assert result == mock_conn

    @patch('core.database._connect')
    def test_get_db_connection_already_connected(self, mock_connect):
        """Test getting connection when already connected."""
        import core.database
        mock_conn = MagicMock()
        mock_conn.closed = 0  # Open connection
        core.database._CONN = mock_conn
        
        result = get_db_connection()
        
        mock_connect.assert_not_called()
        assert result == mock_conn

    @patch('core.database._connect')
    def test_get_db_connection_reconnect_closed(self, mock_connect):
        """Test reconnecting when connection is closed."""
        import core.database
        mock_old_conn = MagicMock()
        mock_old_conn.closed = 1  # Closed connection
        core.database._CONN = mock_old_conn
        
        mock_new_conn = MagicMock()
        mock_new_conn.closed = 0
        mock_connect.side_effect = lambda: setattr(core.database, '_CONN', mock_new_conn)
        
        result = get_db_connection()
        
        mock_connect.assert_called_once()
        assert result == mock_new_conn

    @patch('core.database._connect')
    def test_get_db_connection_reconnect_none(self, mock_connect):
        """Test connecting when _CONN is None."""
        import core.database
        core.database._CONN = None
        
        mock_conn = MagicMock()
        mock_conn.closed = 0
        mock_connect.side_effect = lambda: setattr(core.database, '_CONN', mock_conn)
        
        result = get_db_connection()
        
        mock_connect.assert_called_once()
        assert result == mock_conn

class TestDbCursor:
    
    @patch('core.database.get_db_connection')
    def test_db_cursor_success(self, mock_get_conn):
        """Test successful cursor context manager usage."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn
        
        with db_cursor() as cursor:
            cursor.execute("SELECT 1")
        
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT 1")
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('core.database.get_db_connection')
    def test_db_cursor_exception_rollback(self, mock_get_conn):
        """Test cursor rollback on exception."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = DatabaseError("Query failed")
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn
        
        with pytest.raises(DatabaseError, match="Query failed"):
            with db_cursor() as cursor:
                cursor.execute("SELECT 1")
        
        mock_conn.rollback.assert_called_once()
        mock_conn.commit.assert_not_called()
        mock_cursor.close.assert_called_once()

    @patch('core.database.get_db_connection')
    @patch('core.database._connect')
    def test_db_cursor_connection_error_reconnect(self, mock_connect, mock_get_conn):
        """Test cursor handling of connection drops with reconnect."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = OperationalError("Connection lost")
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn
        
        with pytest.raises(OperationalError, match="Connection lost"):
            with db_cursor() as cursor:
                cursor.execute("SELECT 1")
        
        # Should attempt to close old connection and reconnect
        mock_conn.close.assert_called_once()
        mock_connect.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('core.database.get_db_connection')
    @patch('core.database._connect')
    def test_db_cursor_interface_error_reconnect(self, mock_connect, mock_get_conn):
        """Test cursor handling of interface errors with reconnect."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = InterfaceError("Interface error")
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn
        
        with pytest.raises(InterfaceError, match="Interface error"):
            with db_cursor() as cursor:
                cursor.execute("SELECT 1")
        
        # Should attempt to close old connection and reconnect
        mock_conn.close.assert_called_once()
        mock_connect.assert_called_once()

    @patch('core.database.get_db_connection')
    def test_db_cursor_close_cursor_exception(self, mock_get_conn):
        """Test cursor cleanup when cursor.close() fails."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.close.side_effect = Exception("Close failed")
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn
        
        # Should not raise exception even if cursor.close() fails
        with db_cursor() as cursor:
            cursor.execute("SELECT 1")
        
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

class TestExecMany:
    
    @patch('core.database.db_cursor')
    def test_exec_many_success(self, mock_db_cursor):
        """Test successful batch insert."""
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        sql = "INSERT INTO committees (id, name) VALUES (%s, %s)"
        rows = [('C001', 'Committee 1'), ('C002', 'Committee 2')]
        
        exec_many(sql, rows)
        
        mock_cursor.executemany.assert_called_once_with(sql, rows)

    @patch('core.database.db_cursor')
    def test_exec_many_empty_rows(self, mock_db_cursor):
        """Test batch insert with empty rows."""
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        sql = "INSERT INTO committees (id, name) VALUES (%s, %s)"
        rows = []
        
        exec_many(sql, rows)
        
        mock_cursor.executemany.assert_called_once_with(sql, rows)

    @patch('core.database.db_cursor')
    def test_exec_many_database_error(self, mock_db_cursor):
        """Test batch insert with database error."""
        mock_cursor = MagicMock()
        mock_cursor.executemany.side_effect = DatabaseError("Batch insert failed")
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        mock_db_cursor.return_value.__exit__.side_effect = lambda *args: None
        
        sql = "INSERT INTO committees (id, name) VALUES (%s, %s)"
        rows = [('C001', 'Committee 1')]
        
        with pytest.raises(DatabaseError, match="Batch insert failed"):
            exec_many(sql, rows)

class TestExecOne:
    
    @patch('core.database.db_cursor')
    def test_exec_one_with_params(self, mock_db_cursor):
        """Test single query execution with parameters."""
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        sql = "INSERT INTO committees (id, name) VALUES (%s, %s)"
        params = ('C001', 'Test Committee')
        
        exec_one(sql, params)
        
        mock_cursor.execute.assert_called_once_with(sql, params)

    @patch('core.database.db_cursor')
    def test_exec_one_without_params(self, mock_db_cursor):
        """Test single query execution without parameters."""
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        sql = "SELECT COUNT(*) FROM committees"
        
        exec_one(sql)
        
        mock_cursor.execute.assert_called_once_with(sql, None)

    @patch('core.database.db_cursor')
    def test_exec_one_database_error(self, mock_db_cursor):
        """Test single query with database error."""
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = DatabaseError("Query failed")
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        mock_db_cursor.return_value.__exit__.side_effect = lambda *args: None
        
        sql = "SELECT * FROM nonexistent_table"
        
        with pytest.raises(DatabaseError, match="Query failed"):
            exec_one(sql)

class TestDatabaseIntegration:
    """Integration-style tests combining multiple components."""
    
    @patch('core.database.get_db_connection')
    def test_multiple_operations_same_connection(self, mock_get_conn):
        """Test multiple database operations using the same connection."""
        mock_conn = MagicMock()
        mock_cursor1 = MagicMock()
        mock_cursor2 = MagicMock()
        mock_conn.cursor.side_effect = [mock_cursor1, mock_cursor2]
        mock_get_conn.return_value = mock_conn
        
        # First operation
        with db_cursor() as cursor:
            cursor.execute("INSERT INTO committees (id) VALUES (%s)", ('C001',))
        
        # Second operation
        with db_cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM committees")
        
        # Should use same connection for both
        assert mock_get_conn.call_count == 2
        mock_conn.commit.assert_has_calls([call(), call()])

    @patch.dict('os.environ', {
        'DB_HOST': 'localhost',
        'DB_NAME': 'test_db',
        'DB_USER': 'test_user',
        'DB_PASSWORD': 'test_pass',
        'DB_PORT': '5432'
    })
    @patch('core.database.psycopg2.connect')
    def test_full_connection_flow(self, mock_connect):
        """Test complete connection flow from DSN to query execution."""
        import core.database
        core.database._DSN = None
        core.database._CONN = None
        
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.closed = 0
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        # This should trigger DSN creation, connection, and query execution
        with db_cursor() as cursor:
            cursor.execute("SELECT 1")
        
        # Verify DSN was built correctly
        call_args = mock_connect.call_args[0][0]
        assert "host=localhost" in call_args
        assert "dbname=test_db" in call_args
        assert "user=test_user" in call_args
        assert "password=test_pass" in call_args
        
        # Verify query was executed
        mock_cursor.execute.assert_called_once_with("SELECT 1")
        mock_conn.commit.assert_called_once()

    @patch('core.database.db_cursor')
    def test_batch_vs_single_operations(self, mock_db_cursor):
        """Test difference between batch and single operations."""
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        # Test single operation
        exec_one("INSERT INTO committees (id) VALUES (%s)", ('C001',))
        
        # Test batch operation
        rows = [('C002',), ('C003',), ('C004',)]
        exec_many("INSERT INTO committees (id) VALUES (%s)", rows)
        
        # Verify correct methods were called
        mock_cursor.execute.assert_called_once()
        mock_cursor.executemany.assert_called_once()

class TestErrorScenarios:
    """Test various error scenarios and edge cases."""
    
    @patch('core.database._get_dsn')
    def test_dsn_creation_error_propagation(self, mock_get_dsn):
        """Test that DSN creation errors are properly propagated."""
        mock_get_dsn.side_effect = ValueError("Invalid configuration")
        
        # Reset connection to force DSN creation
        import core.database
        core.database._CONN = None
        
        with pytest.raises(ValueError, match="Invalid configuration"):
            get_db_connection()

    @patch('core.database.get_db_connection')
    def test_connection_close_failure_ignored(self, mock_get_conn):
        """Test that connection close failures are ignored during reconnect."""
        import core.database
        
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_conn.close.side_effect = Exception("Close failed")
        mock_cursor.execute.side_effect = OperationalError("Connection lost")
        mock_get_conn.return_value = mock_conn
        
        with patch('core.database._connect') as mock_connect:
            with pytest.raises(OperationalError):
                with db_cursor() as cursor:
                    cursor.execute("SELECT 1")
            
            # Should attempt to close despite the exception
            mock_conn.close.assert_called_once()
            mock_connect.assert_called_once()