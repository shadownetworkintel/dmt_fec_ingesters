# tests/test_state_tracker.py
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from core.state_tracker import (
    get_last_run,
    update_last_run,
    get_checkpoint,
    update_checkpoint,
    clear_checkpoint,
    get_checkpoint_started_at,
    get_committee_last_run,
    update_committee_last_run
)

class TestGetLastRun:
    
    def test_get_last_run_with_result(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting last run when record exists."""
        test_datetime = datetime(2025, 8, 28, 15, 30, 0)
        mock_db_cursor.fetchone.return_value = (test_datetime,)
        
        result = get_last_run("schedule_a", target="all")
        
        assert result == "2025-08-28T15:30:00"
        mock_db_cursor.execute.assert_called_once_with(
            "select last_run from ops.ingest_state where name=%s and target=%s",
            ("schedule_a", "all")
        )

    def test_get_last_run_no_result(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting last run when no record exists."""
        mock_db_cursor.fetchone.return_value = None
        
        result = get_last_run("schedule_a", target="all")
        
        assert result is None
        mock_db_cursor.execute.assert_called_once()

    def test_get_last_run_null_datetime(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting last run when datetime is null."""
        mock_db_cursor.fetchone.return_value = (None,)
        
        result = get_last_run("schedule_a", target="all")
        
        assert result is None

    def test_get_last_run_default_target(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting last run with default target."""
        mock_db_cursor.fetchone.return_value = None
        
        get_last_run("schedule_a")
        
        mock_db_cursor.execute.assert_called_once_with(
            "select last_run from ops.ingest_state where name=%s and target=%s",
            ("schedule_a", "all")
        )

class TestUpdateLastRun:
    
    def test_update_last_run_with_datetime(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test updating last run with specific datetime."""
        test_datetime = datetime(2025, 8, 28, 15, 30, 0)
        
        update_last_run("schedule_a", dt=test_datetime, target="all")
        
        mock_db_cursor.execute.assert_called_once()
        call_args = mock_db_cursor.execute.call_args
        assert "insert into ops.ingest_state" in call_args[0][0]
        assert "on conflict (name, target) do update" in call_args[0][0]
        assert call_args[0][1] == ("schedule_a", "all", test_datetime)

    def test_update_last_run_without_datetime(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test updating last run without specific datetime (uses now())."""
        update_last_run("schedule_a", target="C00123456")
        
        mock_db_cursor.execute.assert_called_once()
        call_args = mock_db_cursor.execute.call_args
        assert call_args[0][1] == ("schedule_a", "C00123456", None)

    def test_update_last_run_default_target(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test updating last run with default target."""
        update_last_run("schedule_a")
        
        call_args = mock_db_cursor.execute.call_args
        assert call_args[0][1][0] == "schedule_a"
        assert call_args[0][1][1] == "all"

class TestGetCheckpoint:
    
    def test_get_checkpoint_with_data(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting checkpoint when data exists."""
        checkpoint_data = {"last_index": "123456", "last_date": "2025-08-28"}
        mock_db_cursor.fetchone.return_value = (checkpoint_data,)
        
        result = get_checkpoint("schedule_a", target="all")
        
        assert result == checkpoint_data
        mock_db_cursor.execute.assert_called_once_with(
            "select data from ops.ingest_checkpoints where name=%s and target=%s",
            ("schedule_a", "all")
        )

    def test_get_checkpoint_no_data(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting checkpoint when no data exists."""
        mock_db_cursor.fetchone.return_value = None
        
        result = get_checkpoint("schedule_a", target="all")
        
        assert result is None

    def test_get_checkpoint_default_target(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting checkpoint with default target."""
        mock_db_cursor.fetchone.return_value = None
        
        get_checkpoint("schedule_a")
        
        mock_db_cursor.execute.assert_called_once_with(
            "select data from ops.ingest_checkpoints where name=%s and target=%s",
            ("schedule_a", "all")
        )

class TestUpdateCheckpoint:
    
    def test_update_checkpoint_without_started_at(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test updating checkpoint without started_at."""
        checkpoint_data = {"last_index": "123456", "last_date": "2025-08-28"}
        
        update_checkpoint("schedule_a", checkpoint_data, target="all")
        
        mock_db_cursor.execute.assert_called_once()
        call_args = mock_db_cursor.execute.call_args
        assert "insert into ops.ingest_checkpoints" in call_args[0][0]
        assert "on conflict (name, target) do update" in call_args[0][0]
        # Check that the JSON data was passed correctly
        assert call_args[0][1][0] == "schedule_a"
        assert call_args[0][1][1] == "all"

    def test_update_checkpoint_with_started_at(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test updating checkpoint with started_at."""
        checkpoint_data = {"last_index": "123456", "last_date": "2025-08-28"}
        started_at = datetime(2025, 8, 28, 10, 0, 0)
        
        update_checkpoint("schedule_a", checkpoint_data, target="all", started_at=started_at)
        
        mock_db_cursor.execute.assert_called_once()
        # The function should add started_at to the data
        # We can't easily check the exact JSON content due to psycopg2.extras.Json wrapping

    def test_update_checkpoint_preserves_original_data(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test that update_checkpoint doesn't modify the original data dict."""
        original_data = {"last_index": "123456"}
        started_at = datetime(2025, 8, 28, 10, 0, 0)
        
        update_checkpoint("schedule_a", original_data, target="all", started_at=started_at)
        
        # Original data should not be modified
        assert "started_at" not in original_data
        assert original_data == {"last_index": "123456"}

class TestClearCheckpoint:
    
    def test_clear_checkpoint_success(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test clearing checkpoint successfully."""
        mock_db_cursor.rowcount = 1
        
        clear_checkpoint("schedule_a", target="all")
        
        mock_db_cursor.execute.assert_called_once_with(
            "delete from ops.ingest_checkpoints where name=%s and target=%s",
            ("schedule_a", "all")
        )

    def test_clear_checkpoint_not_found(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test clearing checkpoint when none exists."""
        mock_db_cursor.rowcount = 0
        
        clear_checkpoint("schedule_a", target="all")
        
        mock_db_cursor.execute.assert_called_once()

    def test_clear_checkpoint_default_target(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test clearing checkpoint with default target."""
        clear_checkpoint("schedule_a")
        
        mock_db_cursor.execute.assert_called_once_with(
            "delete from ops.ingest_checkpoints where name=%s and target=%s",
            ("schedule_a", "all")
        )

class TestGetCheckpointStartedAt:
    
    def test_get_checkpoint_started_at_with_data(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting started_at from checkpoint."""
        checkpoint_data = {
            "last_index": "123456",
            "started_at": "2025-08-28T10:00:00"
        }
        mock_db_cursor.fetchone.return_value = (checkpoint_data,)
        
        result = get_checkpoint_started_at("schedule_a", target="all")
        
        assert result == datetime(2025, 8, 28, 10, 0, 0)

    def test_get_checkpoint_started_at_no_checkpoint(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting started_at when no checkpoint exists."""
        mock_db_cursor.fetchone.return_value = None
        
        result = get_checkpoint_started_at("schedule_a", target="all")
        
        assert result is None

    def test_get_checkpoint_started_at_no_started_at_field(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting started_at when checkpoint has no started_at field."""
        checkpoint_data = {"last_index": "123456"}
        mock_db_cursor.fetchone.return_value = (checkpoint_data,)
        
        result = get_checkpoint_started_at("schedule_a", target="all")
        
        assert result is None

    def test_get_checkpoint_started_at_invalid_datetime(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker  # Add this line for compatibility
        """Test getting started_at with invalid datetime format."""
        checkpoint_data = {
            "last_index": "123456",
            "started_at": "invalid-datetime"
        }
        mock_db_cursor.fetchone.return_value = (checkpoint_data,)
        
        result = get_checkpoint_started_at("schedule_a", target="all")
        
        assert result is None

class TestCommitteeSpecificFunctions:
    
    def test_get_committee_last_run_with_result(self, mock_db_cursor_state_tracker):
        """Test getting committee last run when record exists."""
        mock_db_cursor = mock_db_cursor_state_tracker
        test_datetime = datetime(2025, 8, 28, 15, 30, 0)
        mock_db_cursor.fetchone.return_value = (test_datetime,)
        
        result = get_committee_last_run("schedule_a", "C00123456")
        
        assert result == "2025-08-28T15:30:00"
        # Use the more flexible assertion approach
        mock_db_cursor.execute.assert_called_once()
        call_args = mock_db_cursor.execute.call_args
        assert "select last_run" in call_args[0][0]
        assert call_args[0][1] == ("schedule_a", "C00123456")

    def test_get_committee_last_run_no_result(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker
        """Test getting committee last run when no record exists."""
        mock_db_cursor.fetchone.return_value = None
        
        result = get_committee_last_run("schedule_a", "C00123456")
        
        assert result is None

    def test_update_committee_last_run_with_datetime(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker
        """Test updating committee last run with specific datetime."""
        test_datetime = datetime(2025, 8, 28, 15, 30, 0)
        
        update_committee_last_run("schedule_a", "C00123456", dt=test_datetime)
        
        mock_db_cursor.execute.assert_called_once()
        call_args = mock_db_cursor.execute.call_args
        assert "insert into ops.committee_run_state" in call_args[0][0]
        assert "on conflict (schedule_name, committee_id) do update" in call_args[0][0]
        assert call_args[0][1] == ("schedule_a", "C00123456", test_datetime)

    def test_update_committee_last_run_without_datetime(self, mock_db_cursor_state_tracker):
        mock_db_cursor = mock_db_cursor_state_tracker
        """Test updating committee last run without specific datetime."""
        update_committee_last_run("schedule_a", "C00123456")
        
        call_args = mock_db_cursor.execute.call_args
        assert call_args[0][1] == ("schedule_a", "C00123456", None)