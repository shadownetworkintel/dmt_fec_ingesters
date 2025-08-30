# tests/test_utils.py
import pytest
from unittest.mock import patch, MagicMock
from core.utils import (
    load_committee_list,
    add_committee_target,
    remove_committee_target,
    list_committee_targets,
    enable_all_committees_mode
)

class TestLoadCommitteeList:
    
    def test_load_committee_list_with_active_committees(self, mock_db_cursor, sample_committee_data):
        """Test loading committee list with active committees."""
        mock_db_cursor.fetchall.return_value = sample_committee_data
        
        result = load_committee_list()
        
        assert result == ['C00467571', 'C00524728', 'C00639591']
        mock_db_cursor.execute.assert_called_once()
        assert "SELECT committee_id" in mock_db_cursor.execute.call_args[0][0]
        assert "WHERE active = TRUE" in mock_db_cursor.execute.call_args[0][0]

    def test_load_committee_list_no_active_committees(self, mock_db_cursor, empty_committee_data):
        """Test loading committee list when no active committees exist."""
        mock_db_cursor.fetchall.return_value = empty_committee_data
        
        result = load_committee_list()
        
        assert result is None
        mock_db_cursor.execute.assert_called_once()

    def test_load_committee_list_filters_none_values(self, mock_db_cursor):
        """Test that None values are filtered out."""
        mock_db_cursor.fetchall.return_value = [('C00467571',), (None,), ('C00524728',)]
        
        result = load_committee_list()
        
        assert result == ['C00467571', 'C00524728']

    def test_load_committee_list_database_error(self, mock_db_cursor):
        """Test handling of database errors."""
        mock_db_cursor.execute.side_effect = Exception("Database connection failed")
        
        result = load_committee_list()
        
        assert result is None

class TestAddCommitteeTarget:
    
    def test_add_committee_target_success(self, mock_db_cursor):
        """Test successfully adding a committee target."""
        result = add_committee_target("C00123456", "Test Committee", "Test description")
        
        assert result is True
        mock_db_cursor.execute.assert_called_once()
        call_args = mock_db_cursor.execute.call_args
        assert "INSERT INTO ops.committee_targets" in call_args[0][0]
        assert call_args[0][1] == ("C00123456", "Test Committee", "Test description")

    def test_add_committee_target_minimal_params(self, mock_db_cursor):
        """Test adding committee target with minimal parameters."""
        result = add_committee_target("C00123456")
        
        assert result is True
        call_args = mock_db_cursor.execute.call_args
        assert call_args[0][1] == ("C00123456", None, None)

    def test_add_committee_target_database_error(self, mock_db_cursor):
        """Test handling database errors when adding committee target."""
        mock_db_cursor.execute.side_effect = Exception("Database error")
        
        result = add_committee_target("C00123456")
        
        assert result is False

class TestRemoveCommitteeTarget:
    
    def test_remove_committee_target_success(self, mock_db_cursor):
        """Test successfully removing a committee target."""
        mock_db_cursor.rowcount = 1
        
        result = remove_committee_target("C00123456")
        
        assert result is True
        mock_db_cursor.execute.assert_called_once()
        call_args = mock_db_cursor.execute.call_args
        assert "UPDATE ops.committee_targets" in call_args[0][0]
        assert "SET active = FALSE" in call_args[0][0]
        assert call_args[0][1] == ("C00123456",)

    def test_remove_committee_target_not_found(self, mock_db_cursor):
        """Test removing non-existent committee target."""
        mock_db_cursor.rowcount = 0
        
        result = remove_committee_target("C00123456")
        
        assert result is False

    def test_remove_committee_target_database_error(self, mock_db_cursor):
        """Test handling database errors when removing committee target."""
        mock_db_cursor.execute.side_effect = Exception("Database error")
        
        result = remove_committee_target("C00123456")
        
        assert result is False

class TestListCommitteeTargets:
    
    def test_list_committee_targets_success(self, mock_db_cursor, sample_committee_targets):
        """Test successfully listing committee targets."""
        # Mock the database rows (tuples)
        mock_rows = [
            ('C00467571', 'ANDY BARR FOR SENATE, INC.', 'H0KY06104, S6KY00286', True, sample_committee_targets[0]['created_at'], sample_committee_targets[0]['updated_at']),
            ('C00639591', 'ALEXANDRIA OCASIO-CORTEZ FOR CONGRESS', 'H8NY15148', False, sample_committee_targets[1]['created_at'], sample_committee_targets[1]['updated_at'])
        ]
        mock_db_cursor.fetchall.return_value = mock_rows
        
        result = list_committee_targets()
        
        assert len(result) == 2
        assert result[0]['committee_id'] == 'C00467571'
        assert result[0]['active'] is True
        assert result[1]['committee_id'] == 'C00639591'
        assert result[1]['active'] is False

    def test_list_committee_targets_empty(self, mock_db_cursor):
        """Test listing committee targets when none exist."""
        mock_db_cursor.fetchall.return_value = []
        
        result = list_committee_targets()
        
        assert result == []

    def test_list_committee_targets_database_error(self, mock_db_cursor):
        """Test handling database errors when listing committee targets."""
        mock_db_cursor.execute.side_effect = Exception("Database error")
        
        result = list_committee_targets()
        
        assert result == []

class TestEnableAllCommitteesMode:
    
    def test_enable_all_committees_mode_success(self, mock_db_cursor):
        """Test successfully enabling all committees mode."""
        mock_db_cursor.rowcount = 3
        
        result = enable_all_committees_mode()
        
        assert result is True
        mock_db_cursor.execute.assert_called_once()
        call_args = mock_db_cursor.execute.call_args
        assert "UPDATE ops.committee_targets" in call_args[0][0]
        assert "SET active = FALSE" in call_args[0][0]

    def test_enable_all_committees_mode_database_error(self, mock_db_cursor):
        """Test handling database errors when enabling all committees mode."""
        mock_db_cursor.execute.side_effect = Exception("Database error")
        
        result = enable_all_committees_mode()
        
        assert result is False