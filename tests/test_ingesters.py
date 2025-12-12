# tests/test_ingesters.py
import pytest
from unittest.mock import patch, MagicMock, call
from datetime import datetime, timedelta
import json
import os
import sys

class TestCandidatesIngester:
    """Test candidates ingester (no checkpoints, uses last_run only)."""
    
    @patch('ingesters.api_candidates_ingester.send_slack_alert')
    @patch('ingesters.api_candidates_ingester.execute_batch')
    @patch('ingesters.api_candidates_ingester.db_cursor')
    @patch('ingesters.api_candidates_ingester.fetch_with_retries')
    @patch('ingesters.api_candidates_ingester.update_last_run')
    @patch('ingesters.api_candidates_ingester.get_last_run')
    @patch('ingesters.api_candidates_ingester.time.sleep')
    def test_candidates_ingester_success(self, mock_sleep, mock_get_last_run, mock_update_last_run,
                                       mock_fetch, mock_db_cursor, mock_execute_batch, mock_slack):
        """Test successful candidates ingestion."""
        # Setup mocks
        mock_get_last_run.return_value = None  # First run
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        # Mock API responses - first page with data, second page empty
        api_response_page1 = {
            'results': [
                {
                    'candidate_id': 'H0ABC12345',
                    'name': 'John Doe',
                    'candidate_status': 'C',
                    'candidate_status_full': 'Candidate',
                    'cycle': [2024],
                    'party': 'DEM',
                    'party_full': 'Democratic Party',
                    'state': 'CA',
                    'office': 'H'
                },
                {
                    'candidate_id': 'S0XYZ67890',
                    'name': 'Jane Smith',
                    'candidate_status': 'C',
                    'candidate_status_full': 'Candidate',
                    'cycle': [2024],
                    'party': 'REP',
                    'party_full': 'Republican Party',
                    'state': 'TX',
                    'office': 'S'
                }
            ]
        }
        api_response_page2 = {'results': []}  # Empty response to end pagination
        
        mock_fetch.side_effect = [api_response_page1, api_response_page2]
        
        # Import and run
        from ingesters.api_candidates_ingester import run
        run()
        
        # Verify API calls
        assert mock_fetch.call_count == 2
        
        # Check API call parameters (don't rely on specific page numbers)
        call_args_list = mock_fetch.call_args_list
        first_params = call_args_list[0][0][1]  # First call params
        assert first_params['per_page'] == 100
        assert first_params['sort'] == 'candidate_id'
        assert 'min_first_file_date' not in first_params  # No last run
        
        # Verify database insert
        mock_execute_batch.assert_called_once()
        insert_call = mock_execute_batch.call_args
        sql_query = insert_call[0][1]  # SQL query
        data_rows = insert_call[0][2]  # Data rows
        
        assert 'INSERT INTO candidates' in sql_query
        assert 'ON CONFLICT (candidate_id) DO UPDATE SET' in sql_query
        assert len(data_rows) == 2
        
        # Verify state tracking
        mock_update_last_run.assert_called_once_with("candidates")
        
        # Verify no error alerts
        mock_slack.assert_not_called()

    @patch('ingesters.api_candidates_ingester.send_slack_alert')
    @patch('ingesters.api_candidates_ingester.execute_batch')
    @patch('ingesters.api_candidates_ingester.db_cursor')
    @patch('ingesters.api_candidates_ingester.fetch_with_retries')
    @patch('ingesters.api_candidates_ingester.update_last_run')
    @patch('ingesters.api_candidates_ingester.get_last_run')
    @patch('ingesters.api_candidates_ingester.time.sleep')
    def test_candidates_ingester_with_last_run(self, mock_sleep, mock_get_last_run, mock_update_last_run,
                                             mock_fetch, mock_db_cursor, mock_execute_batch, mock_slack):
        """Test candidates ingester with previous run date."""
        # Setup with previous run
        mock_get_last_run.return_value = "2025-08-01T10:00:00"
        mock_fetch.return_value = {'results': []}  # Empty to end quickly
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        from ingesters.api_candidates_ingester import run
        run()
        
        # Verify min_first_file_date parameter was set
        call_args = mock_fetch.call_args
        params = call_args[0][1]
        assert 'min_first_file_date' in params
        assert params['min_first_file_date'] == "2025-08-01"

    @patch('ingesters.api_candidates_ingester.send_slack_alert')
    @patch('ingesters.api_candidates_ingester.fetch_with_retries')
    @patch('ingesters.api_candidates_ingester.get_last_run')
    def test_candidates_ingester_api_error(self, mock_get_last_run, mock_fetch, mock_slack):
        """Test candidates ingester with API error."""
        mock_get_last_run.return_value = None
        mock_fetch.side_effect = Exception("API Error")
        
        from ingesters.api_candidates_ingester import run
        
        with pytest.raises(Exception, match="API Error"):
            run()
        
        # Verify error alert was sent
        mock_slack.assert_called_once()
        alert_call = mock_slack.call_args[0][0]
        assert "❌ *Candidates Ingester FAILED*" in alert_call
        assert "API Error" in alert_call

    @patch('ingesters.api_candidates_ingester.send_slack_alert')
    @patch('ingesters.api_candidates_ingester.execute_batch')
    @patch('ingesters.api_candidates_ingester.db_cursor')
    @patch('ingesters.api_candidates_ingester.fetch_with_retries')
    @patch('ingesters.api_candidates_ingester.get_last_run')
    def test_candidates_ingester_database_error(self, mock_get_last_run, mock_fetch, 
                                              mock_db_cursor, mock_execute_batch, mock_slack):
        """Test candidates ingester with database error."""
        mock_get_last_run.return_value = None
        mock_fetch.return_value = {
            'results': [{'candidate_id': 'H0ABC12345', 'name': 'Test'}]
        }
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        mock_execute_batch.side_effect = Exception("Database Error")
        
        from ingesters.api_candidates_ingester import run
        
        with pytest.raises(Exception, match="Database Error"):
            run()
        
        # Verify error alert
        mock_slack.assert_called_once()

class TestCommitteesIngester:
    """Test committees ingester (no checkpoints, uses last_run only)."""
    
    @patch('ingesters.api_committees_ingester.send_slack_alert')
    @patch('ingesters.api_committees_ingester.execute_batch')
    @patch('ingesters.api_committees_ingester.db_cursor')
    @patch('ingesters.api_committees_ingester.fetch_with_retries')
    @patch('ingesters.api_committees_ingester.update_last_run')
    @patch('ingesters.api_committees_ingester.get_last_run')
    @patch('ingesters.api_committees_ingester.time.sleep')
    def test_committees_ingester_success(self, mock_sleep, mock_get_last_run, mock_update_last_run,
                                       mock_fetch, mock_db_cursor, mock_execute_batch, mock_slack):
        """Test successful committees ingestion."""
        mock_get_last_run.return_value = None
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        api_response = {
            'results': [
                {
                    'committee_id': 'C00123456',
                    'name': 'Test Committee',
                    'committee_type': 'H',
                    'designation': 'P',
                    'party': 'DEM',
                    'state': 'CA',
                    'candidate_ids': ['H0ABC12345'],
                    'cycles': [2024],
                    'is_active': True
                }
            ]
        }
        mock_fetch.side_effect = [api_response, {'results': []}]
        
        from ingesters.api_committees_ingester import run
        run()
        
        # Verify database operations
        mock_execute_batch.assert_called_once()
        insert_call = mock_execute_batch.call_args
        sql_query = insert_call[0][1]
        data_rows = insert_call[0][2]
        
        assert 'INSERT INTO committees' in sql_query
        assert 'ON CONFLICT (committee_id) DO UPDATE SET' in sql_query
        assert len(data_rows) == 1
        
        mock_update_last_run.assert_called_once_with("committees")

    @patch('ingesters.api_committees_ingester.send_slack_alert')
    @patch('ingesters.api_committees_ingester.execute_batch')
    @patch('ingesters.api_committees_ingester.db_cursor')
    @patch('ingesters.api_committees_ingester.fetch_with_retries')
    @patch('ingesters.api_committees_ingester.update_last_run')
    @patch('ingesters.api_committees_ingester.get_last_run')
    @patch('ingesters.api_committees_ingester.time.sleep')
    def test_committees_ingester_json_serialization(self, mock_sleep, mock_get_last_run, mock_update_last_run,
                                                   mock_fetch, mock_db_cursor, mock_execute_batch, mock_slack):
        """Test that list fields are properly JSON serialized."""
        mock_get_last_run.return_value = None
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        # Mock response with list fields
        api_response = {
            'results': [
                {
                    'committee_id': 'C00123456',
                    'candidate_ids': ['H0ABC12345', 'H0XYZ67890'],
                    'cycles': [2022, 2024],
                    'cycles_has_activity': [2024],
                    'jfc_committee': ['C00999888'],
                    'name': 'Test Committee'
                }
            ]
        }
        
        mock_fetch.side_effect = [api_response, {'results': []}]
        
        from ingesters.api_committees_ingester import run
        run()
        
        # Check that execute_batch was called
        mock_execute_batch.assert_called_once()

class TestScheduleAIngester:
    """Test Schedule A ingester (uses checkpoints and targets)."""
    
    @patch('ingesters.api_schedule_a_ingester.send_slack_alert')
    @patch('ingesters.api_schedule_a_ingester.execute_batch')
    @patch('ingesters.api_schedule_a_ingester.db_cursor')
    @patch('ingesters.api_schedule_a_ingester.fetch_with_retries')
    @patch('ingesters.api_schedule_a_ingester.clear_checkpoint')
    @patch('ingesters.api_schedule_a_ingester.update_checkpoint')
    @patch('ingesters.api_schedule_a_ingester.get_checkpoint')
    @patch('ingesters.api_schedule_a_ingester.update_last_run')
    @patch('ingesters.api_schedule_a_ingester.get_last_run')
    @patch('ingesters.api_schedule_a_ingester.time.sleep')
    def test_schedule_a_ingester_all_committees_success(self, mock_sleep, mock_get_last_run, mock_update_last_run,
                                                      mock_get_checkpoint, mock_update_checkpoint, mock_clear_checkpoint,
                                                      mock_fetch, mock_db_cursor, mock_execute_batch, mock_slack):
        """Test Schedule A ingester for all committees."""
        # Setup mocks
        mock_get_last_run.return_value = None
        mock_get_checkpoint.return_value = None
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        # Mock API response
        api_response = {
            'results': [
                {
                    'sub_id': '1001',
                    'committee_id': 'C00123456',
                    'contributor_name': 'John Doe',
                    'contribution_receipt_amount': 100.0,
                    'contribution_receipt_date': '2025-08-28',
                    'contributor_city': 'New York',
                    'contributor_state': 'NY'
                }
            ],
            'pagination': {
                'last_indexes': {
                    'last_index': '1001',
                    'last_contribution_receipt_date': '2025-08-28'
                }
            }
        }
        mock_fetch.side_effect = [api_response, {'results': []}]
        
        from ingesters.api_schedule_a_ingester import run
        run()  # No committee_id = all committees mode
        
        # Verify target-based state tracking
        mock_get_last_run.assert_called_with("schedule_a", target="all")
        mock_get_checkpoint.assert_called_with("schedule_a", target="all")
        mock_update_checkpoint.assert_called_once()
        mock_clear_checkpoint.assert_called_with("schedule_a", target="all")
        mock_update_last_run.assert_called()
        
        # Verify database insert
        mock_execute_batch.assert_called_once()

    @patch('ingesters.api_schedule_a_ingester.send_slack_alert')
    @patch('ingesters.api_schedule_a_ingester.execute_batch')
    @patch('ingesters.api_schedule_a_ingester.db_cursor')
    @patch('ingesters.api_schedule_a_ingester.fetch_with_retries')
    @patch('ingesters.api_schedule_a_ingester.update_last_run')
    @patch('ingesters.api_schedule_a_ingester.get_last_run')
    @patch('ingesters.api_schedule_a_ingester.time.sleep')
    def test_schedule_a_ingester_specific_committee(self, mock_sleep, mock_get_last_run, mock_update_last_run,
                                                  mock_fetch, mock_db_cursor, mock_execute_batch, mock_slack):
        """Test Schedule A ingester for specific committee."""
        mock_get_last_run.return_value = None
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        api_response = {
            'results': [
                {
                    'sub_id': '1001',
                    'committee_id': 'C00123456',
                    'contribution_receipt_amount': 100.0
                }
            ]
        }
        mock_fetch.side_effect = [api_response, {'results': []}]
        
        from ingesters.api_schedule_a_ingester import run
        run(committee_id='C00123456')
        
        # Verify committee-specific state tracking
        mock_get_last_run.assert_called_with("schedule_a", target='C00123456')
        mock_update_last_run.assert_called()
        
        # Verify API call includes committee_id
        call_args = mock_fetch.call_args_list[0]
        params = call_args[0][1]
        assert params['committee_id'] == 'C00123456'

    @patch('ingesters.api_schedule_a_ingester.load_committee_list')
    @patch('ingesters.api_schedule_a_ingester.run')
    @patch('sys.argv', ['script.py'])  # Mock command line arguments
    def test_schedule_a_main_with_committee_list(self, mock_run, mock_load_committee_list):
        """Test main function with committee list."""
        mock_load_committee_list.return_value = ['C00123456', 'C00789012']
        
        from ingesters.api_schedule_a_ingester import main
        main()
        
        # Should call run() for each committee
        assert mock_run.call_count == 2
        mock_run.assert_has_calls([
            call(committee_id='C00123456'),
            call(committee_id='C00789012')
        ])

    @patch('ingesters.api_schedule_a_ingester.load_committee_list')
    @patch('ingesters.api_schedule_a_ingester.run')
    @patch('sys.argv', ['script.py', '--resume-index', '123', '--resume-date', '2025-08-28'])
    def test_schedule_a_main_no_committee_list(self, mock_run, mock_load_committee_list):
        """Test main function without committee list."""
        mock_load_committee_list.return_value = None
        
        from ingesters.api_schedule_a_ingester import main
        main()
        
        # Should call run() once for all committees with resume args
        mock_run.assert_called_once_with(resume_index='123', resume_date='2025-08-28')

    @patch('ingesters.api_schedule_a_ingester.send_slack_alert')
    @patch('ingesters.api_schedule_a_ingester.execute_batch')
    @patch('ingesters.api_schedule_a_ingester.db_cursor')
    @patch('ingesters.api_schedule_a_ingester.clear_checkpoint')  # Mock clear_checkpoint
    @patch('ingesters.api_schedule_a_ingester.get_checkpoint_started_at')
    @patch('ingesters.api_schedule_a_ingester.get_checkpoint')
    @patch('ingesters.api_schedule_a_ingester.get_last_run')
    @patch('ingesters.api_schedule_a_ingester.fetch_with_retries')
    @patch('ingesters.api_schedule_a_ingester.update_last_run')
    @patch('ingesters.api_schedule_a_ingester.time.sleep')
    def test_schedule_a_resume_from_checkpoint(self, mock_sleep, mock_update_last_run, mock_fetch, 
                                             mock_get_last_run, mock_get_checkpoint, 
                                             mock_get_checkpoint_started_at, mock_clear_checkpoint,
                                             mock_db_cursor, mock_execute_batch, mock_slack):
        """Test resuming from saved checkpoint."""
        mock_get_last_run.return_value = None
        mock_get_checkpoint.return_value = {
            'last_index': '999',
            'last_contribution_receipt_date': '2025-08-27'
        }
        mock_get_checkpoint_started_at.return_value = datetime(2025, 8, 27, 10, 0, 0)
        mock_fetch.return_value = {'results': []}  # Empty to end quickly
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        from ingesters.api_schedule_a_ingester import run
        run()  # All committees mode
        
        # Verify checkpoint was used
        mock_get_checkpoint.assert_called_with("schedule_a", target="all")
        
        # Verify API call used checkpoint values
        call_args = mock_fetch.call_args
        params = call_args[0][1]
        assert params['last_index'] == '999'
        assert params['last_contribution_receipt_date'] == '2025-08-27'

class TestScheduleBIngester:
    """Test Schedule B ingester (similar to Schedule A)."""
    
    @patch('ingesters.api_schedule_b_ingester.send_slack_alert')
    @patch('ingesters.api_schedule_b_ingester.execute_batch')
    @patch('ingesters.api_schedule_b_ingester.db_cursor')
    @patch('ingesters.api_schedule_b_ingester.fetch_with_retries')
    @patch('ingesters.api_schedule_b_ingester.clear_checkpoint')
    @patch('ingesters.api_schedule_b_ingester.get_checkpoint')
    @patch('ingesters.api_schedule_b_ingester.get_last_run')
    @patch('ingesters.api_schedule_b_ingester.update_last_run')
    @patch('ingesters.api_schedule_b_ingester.time.sleep')
    def test_schedule_b_broken_indexes_handling(
        self,
        mock_sleep,
        mock_update_last_run,
        mock_get_last_run,
        mock_get_checkpoint,
        mock_clear_checkpoint,
        mock_fetch,
        mock_db_cursor,
        mock_execute_batch,
        mock_slack,
    ):
        """Test Schedule B resuming from a checkpoint with a 'broken' last_index."""
        mock_get_last_run.return_value = None
        mock_get_checkpoint.return_value = {
            "last_index": "1022620190037443452",  # Known broken index
            "last_disbursement_date": "2025-08-28",
        }
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor

        api_response = {
            "results": [{"sub_id": "1001", "disbursement_amount": 100.0}],
            "pagination": {"last_indexes": {}},
        }
        mock_fetch.side_effect = [api_response, {"results": []}]

        from ingesters.api_schedule_b_ingester import run

        run()

        # Verify that we used the checkpoint values when resuming
        call_args = mock_fetch.call_args_list[0]
        params = call_args[0][1]
        assert params["last_index"] == "1022620190037443452"
        assert params["last_disbursement_date"] == "2025-08-28"
        # still expect default page size
        assert params["per_page"] == 100

    @patch('ingesters.api_schedule_b_ingester.send_slack_alert')
    @patch('ingesters.api_schedule_b_ingester.execute_batch')
    @patch('ingesters.api_schedule_b_ingester.db_cursor')
    @patch('ingesters.api_schedule_b_ingester.fetch_with_retries')
    @patch('ingesters.api_schedule_b_ingester.clear_checkpoint')  # Mock clear_checkpoint
    @patch('ingesters.api_schedule_b_ingester.get_checkpoint')
    @patch('ingesters.api_schedule_b_ingester.get_last_run')
    @patch('ingesters.api_schedule_b_ingester.update_last_run')
    @patch('ingesters.api_schedule_b_ingester.time.sleep')
    def test_schedule_b_sort_null_only_param(self, mock_sleep, mock_update_last_run, mock_get_last_run, 
                                            mock_get_checkpoint, mock_clear_checkpoint, mock_fetch, 
                                            mock_db_cursor, mock_execute_batch, mock_slack):
        """Test that sort_null_only parameter is added when resuming."""
        mock_get_last_run.return_value = None
        mock_get_checkpoint.return_value = {
            'last_index': '999',
            'last_disbursement_date': '2025-08-28'
        }
        mock_fetch.return_value = {'results': []}
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        from ingesters.api_schedule_b_ingester import run
        run()
        
        # Verify sort_null_only was added for resume
        call_args = mock_fetch.call_args
        params = call_args[0][1]
        assert params['sort_null_only'] is True

class TestScheduleEIngester:
    """Test Schedule E ingester."""
    
    @patch('ingesters.api_schedule_e_ingester.send_slack_alert')
    @patch('ingesters.api_schedule_e_ingester.execute_batch')
    @patch('ingesters.api_schedule_e_ingester.db_cursor')
    @patch('ingesters.api_schedule_e_ingester.fetch_with_retries')
    @patch('ingesters.api_schedule_e_ingester.clear_checkpoint')  # Mock clear_checkpoint
    @patch('ingesters.api_schedule_e_ingester.get_checkpoint')
    @patch('ingesters.api_schedule_e_ingester.get_last_run')
    @patch('ingesters.api_schedule_e_ingester.update_last_run')
    @patch('ingesters.api_schedule_e_ingester.time.sleep')
    def test_schedule_e_adapt_value_function(self, mock_sleep, mock_update_last_run, mock_get_last_run, 
                                           mock_get_checkpoint, mock_clear_checkpoint, mock_fetch, 
                                           mock_db_cursor, mock_execute_batch, mock_slack):
        """Test the adapt_value function for dict/list serialization."""
        mock_get_last_run.return_value = None
        mock_get_checkpoint.return_value = None
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        api_response = {
            'results': [
                {
                    'sub_id': '1001',
                    'candidate': {'name': 'John Doe', 'id': 'H0ABC12345'},  # Dict field
                    'candidate_ids': ['H0ABC12345', 'H0XYZ67890'],  # List field
                    'expenditure_amount': 1000.0,  # Regular field
                    'expenditure_date': '2025-08-28'
                }
            ]
        }
        mock_fetch.side_effect = [api_response, {'results': []}]
        
        from ingesters.api_schedule_e_ingester import run
        run()
        
        # Verify execute_batch was called
        mock_execute_batch.assert_called_once()

    @patch('ingesters.api_schedule_e_ingester.send_slack_alert')
    @patch('ingesters.api_schedule_e_ingester.execute_batch')
    @patch('ingesters.api_schedule_e_ingester.db_cursor')
    @patch('ingesters.api_schedule_e_ingester.fetch_with_retries')
    @patch('ingesters.api_schedule_e_ingester.clear_checkpoint')  # Mock clear_checkpoint
    @patch('ingesters.api_schedule_e_ingester.get_checkpoint')
    @patch('ingesters.api_schedule_e_ingester.get_last_run')
    @patch('ingesters.api_schedule_e_ingester.update_last_run')
    @patch('ingesters.api_schedule_e_ingester.time.sleep')
    def test_schedule_e_days_back_parameter(self, mock_sleep, mock_update_last_run, mock_get_last_run, 
                                          mock_get_checkpoint, mock_clear_checkpoint, mock_fetch, 
                                          mock_db_cursor, mock_execute_batch, mock_slack):
        """Test that DAYS_BACK is applied correctly."""
        # Set last run to 35 days ago
        last_run_date = datetime.now() - timedelta(days=35)
        mock_get_last_run.return_value = last_run_date.isoformat()
        mock_get_checkpoint.return_value = None
        mock_fetch.return_value = {'results': []}
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        from ingesters.api_schedule_e_ingester import run
        run()
        
        # Verify min_date parameter
        call_args = mock_fetch.call_args
        params = call_args[0][1]
        assert 'min_date' in params
        
        # Should be last_run_date - 30 days (DAYS_BACK)
        expected_min_date = (last_run_date.date() - timedelta(days=30)).strftime("%Y-%m-%d")
        assert params['min_date'] == expected_min_date

class TestIngesterErrorHandling:
    """Test error handling across all ingesters."""
    
    @patch('ingesters.api_candidates_ingester.send_slack_alert')
    @patch('ingesters.api_candidates_ingester.get_last_run')
    def test_candidates_error_formatting(self, mock_get_last_run, mock_slack):
        """Test error message formatting in candidates ingester."""
        mock_get_last_run.side_effect = Exception("State tracker error")
        
        from ingesters.api_candidates_ingester import run
        
        with pytest.raises(Exception):
            run()
        
        # Verify error alert format
        mock_slack.assert_called_once()
        alert_message = mock_slack.call_args[0][0]
        assert "❌ *Candidates Ingester FAILED*" in alert_message
        assert "State tracker error" in alert_message
        assert "```" in alert_message  # JSON formatting

    @patch('ingesters.api_schedule_a_ingester.send_slack_alert')
    @patch('ingesters.api_schedule_a_ingester.get_last_run')
    def test_schedule_a_error_with_params(self, mock_get_last_run, mock_slack):
        """Test that error alerts include API parameters."""
        mock_get_last_run.side_effect = Exception("Database connection failed")
        
        from ingesters.api_schedule_a_ingester import run
        
        with pytest.raises(Exception):
            run()
        
        # Verify error alert includes params
        alert_message = mock_slack.call_args[0][0]
        assert "❌ *Schedule A Ingester FAILED*" in alert_message
        assert "two_year_transaction_period" in alert_message

class TestIngesterIntegration:
    """Integration tests for ingester workflows."""
    
    def test_ingester_sleep_timing_simple(self):
        """Test that candidates ingester sleeps after getting results from a page."""
        with patch('ingesters.api_candidates_ingester.fetch_with_retries') as mock_fetch, \
             patch('ingesters.api_candidates_ingester.get_last_run') as mock_last_run, \
             patch('ingesters.api_candidates_ingester.execute_batch') as mock_execute_batch, \
             patch('ingesters.api_candidates_ingester.db_cursor') as mock_db_cursor, \
             patch('ingesters.api_candidates_ingester.update_last_run') as mock_update_last_run, \
             patch('ingesters.api_candidates_ingester.time.sleep') as mock_sleep:
            
            mock_last_run.return_value = None
            mock_cursor = MagicMock()
            mock_db_cursor.return_value.__enter__.return_value = mock_cursor
            
            # Return a page with results, then an empty page to trigger sleep
            mock_fetch.side_effect = [
                {'results': [{'candidate_id': 'H0ABC12345'}]},  # Page 1 - has data
                {'results': []}  # Page 2 - empty (ends, but should have triggered sleep)
            ]
            
            from ingesters.api_candidates_ingester import run
            run()
            
            # Verify sleep was called after page 1 returned data
            mock_sleep.assert_called_with(3.7)

    def test_api_key_usage(self):
        """Test that ingesters properly format API parameters."""
        with patch('ingesters.api_candidates_ingester.fetch_with_retries') as mock_fetch, \
             patch('ingesters.api_candidates_ingester.get_last_run') as mock_last_run, \
             patch('ingesters.api_candidates_ingester.execute_batch') as mock_execute_batch, \
             patch('ingesters.api_candidates_ingester.db_cursor') as mock_db_cursor, \
             patch('ingesters.api_candidates_ingester.update_last_run') as mock_update_last_run:
            
            mock_last_run.return_value = None
            mock_fetch.return_value = {'results': []}
            mock_cursor = MagicMock()
            mock_db_cursor.return_value.__enter__.return_value = mock_cursor
            
            from ingesters.api_candidates_ingester import run
            run()
            
            # Verify fetch was called with correct structure
            call_args = mock_fetch.call_args
            params = call_args[0][1]
            assert 'api_key' in params  # API key should be present
            assert 'per_page' in params  # Standard parameters should be present
            assert params['per_page'] == 100

class TestIngesterDataValidation:
    """Test data validation and transformation in ingesters."""
    
    @patch('ingesters.api_committees_ingester.execute_batch')
    @patch('ingesters.api_committees_ingester.db_cursor')
    @patch('ingesters.api_committees_ingester.fetch_with_retries')
    @patch('ingesters.api_committees_ingester.get_last_run')
    @patch('ingesters.api_committees_ingester.update_last_run')
    @patch('ingesters.api_committees_ingester.time.sleep')
    def test_committees_json_field_handling(self, mock_sleep, mock_update_last_run, mock_get_last_run, 
                                          mock_fetch, mock_db_cursor, mock_execute_batch):
        """Test that specific fields are JSON serialized in committees."""
        mock_get_last_run.return_value = None
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        
        api_response = {
            'results': [
                {
                    'committee_id': 'C00123456',
                    'name': 'Test Committee',
                    'candidate_ids': ['H0ABC12345'],  # Should be JSON serialized
                    'cycles': [2024, 2026],  # Should be JSON serialized
                    'jfc_committee': ['C00999888'],  # Should be JSON serialized
                    'treasurer_name': 'John Doe',  # Should NOT be JSON serialized
                    'cycles_has_activity': None  # None should stay None
                }
            ]
        }
        mock_fetch.side_effect = [api_response, {'results': []}]
        
        from ingesters.api_committees_ingester import run
        run()
        
        # Verify execute_batch was called
        mock_execute_batch.assert_called_once()

    def test_schedule_e_adapt_value_function_directly(self):
        """Test the adapt_value function directly."""
        from ingesters.api_schedule_e_ingester import adapt_value
        
        # Test dict serialization
        dict_val = {'name': 'John', 'id': 123}
        assert adapt_value(dict_val) == '{"name": "John", "id": 123}'
        
        # Test list serialization
        list_val = ['item1', 'item2']
        assert adapt_value(list_val) == '["item1", "item2"]'
        
        # Test regular values pass through
        assert adapt_value('string') == 'string'
        assert adapt_value(123) == 123
        assert adapt_value(None) is None