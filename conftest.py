# conftest.py
import pytest
from unittest.mock import MagicMock, patch
import os
from datetime import datetime

@pytest.fixture(autouse=True)
def setup_test_env():
    """Set up test environment variables."""
    os.environ.setdefault("DATABASE_URL", "postgresql://test:test@localhost:5432/test_db")
    os.environ.setdefault("FEC_API_KEY", "test_api_key")
    os.environ.setdefault("ENV_MODE", "test")

@pytest.fixture
def mock_db_cursor():
    """Mock database cursor for testing."""
    with patch('core.utils.db_cursor') as mock_cursor:
        mock_cursor_instance = MagicMock()
        mock_cursor.__enter__ = MagicMock(return_value=mock_cursor_instance)
        mock_cursor.__exit__ = MagicMock(return_value=None)
        mock_cursor.return_value = mock_cursor
        yield mock_cursor_instance

@pytest.fixture
def mock_db_cursor_state_tracker():
    """Mock database cursor specifically for state_tracker tests."""
    with patch('core.state_tracker.db_cursor') as mock_cursor:
        mock_cursor_instance = MagicMock()
        mock_cursor.__enter__ = MagicMock(return_value=mock_cursor_instance)
        mock_cursor.__exit__ = MagicMock(return_value=None)
        mock_cursor.return_value = mock_cursor
        yield mock_cursor_instance

@pytest.fixture
def mock_requests_get():
    """Mock requests.get for fetcher tests."""
    with patch('core.fetcher.requests.get') as mock_get:
        yield mock_get

@pytest.fixture
def sample_api_response():
    """Sample API response for testing."""
    return {
        "results": [
            {"sub_id": "12345", "committee_id": "C00123456", "amount": 100.0},
            {"sub_id": "12346", "committee_id": "C00123456", "amount": 200.0}
        ],
        "pagination": {
            "last_indexes": {"last_index": "67890", "last_date": "2025-08-28"},
            "count": 2,
            "pages": 1
        }
    }

@pytest.fixture
def sample_committee_data():
    """Sample committee data for testing."""
    return [
        ('C00467571',),
        ('C00524728',),
        ('C00639591',),
    ]

@pytest.fixture
def empty_committee_data():
    """Empty committee data for testing."""
    return []

@pytest.fixture
def sample_committee_targets():
    """Sample committee targets with full data."""
    return [
        {
            'committee_id': 'C00467571',
            'committee_name': 'ANDY BARR FOR SENATE, INC.',
            'description': 'H0KY06104, S6KY00286',
            'active': True,
            'created_at': datetime(2025, 8, 28, 10, 0, 0),
            'updated_at': datetime(2025, 8, 28, 10, 0, 0)
        },
        {
            'committee_id': 'C00639591',
            'committee_name': 'ALEXANDRIA OCASIO-CORTEZ FOR CONGRESS',
            'description': 'H8NY15148',
            'active': False,
            'created_at': datetime(2025, 8, 27, 15, 30, 0),
            'updated_at': datetime(2025, 8, 27, 15, 30, 0)
        }
    ]

@pytest.fixture
def mock_slack_response():
    """Mock successful Slack API response."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"ok": True}
    return mock_response

@pytest.fixture
def mock_slack_error_response():
    """Mock Slack API error response."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"ok": False, "error": "channel_not_found"}
    return mock_response

@pytest.fixture
def sample_alert_messages():
    """Sample alert messages for testing."""
    return {
        "database_error": "🚨 Database connection failed during ingestion",
        "ingestion_success": "✅ Successfully ingested 1,500 records from schedule_a",
        "api_error": "⚠️ FEC API rate limit exceeded, retrying in 60 seconds",
        "system_error": "❌ Critical system error: Memory usage at 95%"
    }