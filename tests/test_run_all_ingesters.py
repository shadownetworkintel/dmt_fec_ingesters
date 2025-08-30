import pytest
import sys
import os
from unittest.mock import patch, MagicMock, call
import time

# Add the project root to the Python path so we can import the script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestRunAllIngesters:
    """Test the run_all_ingesters.py script functionality."""
    
    def test_run_all_ingesters_success(self):
        """Test successful execution of all ingesters."""
        with patch('ingesters.api_candidates_ingester.run') as mock_candidates, \
             patch('ingesters.api_committees_ingester.run') as mock_committees, \
             patch('ingesters.api_schedule_a_ingester.main') as mock_schedule_a, \
             patch('ingesters.api_schedule_b_ingester.main') as mock_schedule_b, \
             patch('ingesters.api_schedule_e_ingester.main') as mock_schedule_e:
            
            # Mock all ingesters to succeed
            mock_candidates.return_value = None
            mock_committees.return_value = None
            mock_schedule_a.return_value = None
            mock_schedule_b.return_value = None
            mock_schedule_e.return_value = None
            
            from scripts.run_all_ingesters import main
            main()
            
            # Verify all ingesters were called
            mock_candidates.assert_called_once()
            mock_committees.assert_called_once()
            mock_schedule_a.assert_called_once()
            mock_schedule_b.assert_called_once()
            mock_schedule_e.assert_called_once()

    def test_run_all_ingesters_one_failure(self):
        """Test handling of one ingester failure."""
        with patch('ingesters.api_candidates_ingester.run') as mock_candidates, \
             patch('ingesters.api_committees_ingester.run') as mock_committees, \
             patch('ingesters.api_schedule_a_ingester.main') as mock_schedule_a, \
             patch('ingesters.api_schedule_b_ingester.main') as mock_schedule_b, \
             patch('ingesters.api_schedule_e_ingester.main') as mock_schedule_e:
            
            # Mock schedule_a to fail, others succeed
            mock_candidates.return_value = None
            mock_committees.return_value = None
            mock_schedule_a.side_effect = Exception("Schedule A failed with error")
            mock_schedule_b.return_value = None
            mock_schedule_e.return_value = None
            
            from scripts.run_all_ingesters import main
            main()
            
            # Verify all ingesters were attempted even after failure
            mock_candidates.assert_called_once()
            mock_committees.assert_called_once()
            mock_schedule_a.assert_called_once()
            mock_schedule_b.assert_called_once()
            mock_schedule_e.assert_called_once()

    def test_run_all_ingesters_multiple_failures(self):
        """Test handling of multiple ingester failures."""
        with patch('ingesters.api_candidates_ingester.run') as mock_candidates, \
             patch('ingesters.api_committees_ingester.run') as mock_committees, \
             patch('ingesters.api_schedule_a_ingester.main') as mock_schedule_a, \
             patch('ingesters.api_schedule_b_ingester.main') as mock_schedule_b, \
             patch('ingesters.api_schedule_e_ingester.main') as mock_schedule_e:
            
            # Mock candidates and committees to fail
            mock_candidates.side_effect = Exception("Candidates ingester database error")
            mock_committees.side_effect = Exception("Committees API timeout")
            mock_schedule_a.return_value = None
            mock_schedule_b.return_value = None
            mock_schedule_e.return_value = None
            
            from scripts.run_all_ingesters import main
            main()
            
            # Verify all ingesters were attempted
            mock_candidates.assert_called_once()
            mock_committees.assert_called_once()
            mock_schedule_a.assert_called_once()
            mock_schedule_b.assert_called_once()
            mock_schedule_e.assert_called_once()

    def test_run_all_ingesters_all_failures(self):
        """Test handling when all ingesters fail."""
        with patch('ingesters.api_candidates_ingester.run') as mock_candidates, \
             patch('ingesters.api_committees_ingester.run') as mock_committees, \
             patch('ingesters.api_schedule_a_ingester.main') as mock_schedule_a, \
             patch('ingesters.api_schedule_b_ingester.main') as mock_schedule_b, \
             patch('ingesters.api_schedule_e_ingester.main') as mock_schedule_e:
            
            # Mock all ingesters to fail
            mock_candidates.side_effect = Exception("Candidates failed")
            mock_committees.side_effect = Exception("Committees failed")
            mock_schedule_a.side_effect = Exception("Schedule A failed")
            mock_schedule_b.side_effect = Exception("Schedule B failed")
            mock_schedule_e.side_effect = Exception("Schedule E failed")
            
            from scripts.run_all_ingesters import main
            main()
            
            # Verify all ingesters were attempted
            mock_candidates.assert_called_once()
            mock_committees.assert_called_once()
            mock_schedule_a.assert_called_once()
            mock_schedule_b.assert_called_once()
            mock_schedule_e.assert_called_once()

    def test_ingester_execution_order(self):
        """Test that ingesters run in the correct order."""
        call_order = []
        
        def track_call(name):
            def wrapper(*args, **kwargs):
                call_order.append(name)
            return wrapper
        
        with patch('ingesters.api_candidates_ingester.run', side_effect=track_call('candidates')), \
             patch('ingesters.api_committees_ingester.run', side_effect=track_call('committees')), \
             patch('ingesters.api_schedule_a_ingester.main', side_effect=track_call('schedule_a')), \
             patch('ingesters.api_schedule_b_ingester.main', side_effect=track_call('schedule_b')), \
             patch('ingesters.api_schedule_e_ingester.main', side_effect=track_call('schedule_e')):
            
            from scripts.run_all_ingesters import main
            main()
            
            # Verify execution order
            expected_order = ['candidates', 'committees', 'schedule_a', 'schedule_b', 'schedule_e']
            assert call_order == expected_order

    def test_error_logging(self):
        """Test that errors are properly logged."""
        with patch('ingesters.api_candidates_ingester.run') as mock_candidates, \
             patch('ingesters.api_committees_ingester.run') as mock_committees, \
             patch('ingesters.api_schedule_a_ingester.main') as mock_schedule_a, \
             patch('ingesters.api_schedule_b_ingester.main') as mock_schedule_b, \
             patch('ingesters.api_schedule_e_ingester.main') as mock_schedule_e, \
             patch('scripts.run_all_ingesters.logger') as mock_logger:
            
            # Mock candidates to fail
            mock_candidates.side_effect = Exception("Database connection failed")
            mock_committees.return_value = None
            mock_schedule_a.return_value = None
            mock_schedule_b.return_value = None
            mock_schedule_e.return_value = None
            
            from scripts.run_all_ingesters import main
            main()
            
            # Verify error was logged
            mock_logger.exception.assert_called()
            error_calls = [call for call in mock_logger.exception.call_args_list 
                          if "Candidates Ingester failed" in str(call)]
            assert len(error_calls) > 0

    def test_success_logging(self):
        """Test that successes are properly logged."""
        with patch('ingesters.api_candidates_ingester.run') as mock_candidates, \
             patch('ingesters.api_committees_ingester.run') as mock_committees, \
             patch('ingesters.api_schedule_a_ingester.main') as mock_schedule_a, \
             patch('ingesters.api_schedule_b_ingester.main') as mock_schedule_b, \
             patch('ingesters.api_schedule_e_ingester.main') as mock_schedule_e, \
             patch('scripts.run_all_ingesters.logger') as mock_logger:
            
            # Mock all to succeed
            mock_candidates.return_value = None
            mock_committees.return_value = None
            mock_schedule_a.return_value = None
            mock_schedule_b.return_value = None
            mock_schedule_e.return_value = None
            
            from scripts.run_all_ingesters import main
            main()
            
            # Verify success messages were logged
            info_calls = [str(call) for call in mock_logger.info.call_args_list]
            success_calls = [call for call in info_calls if "completed successfully" in call]
            assert len(success_calls) == 5  # All 5 ingesters succeeded

    def test_pipeline_start_end_logging(self):
        """Test that pipeline start and end are logged."""
        with patch('ingesters.api_candidates_ingester.run'), \
             patch('ingesters.api_committees_ingester.run'), \
             patch('ingesters.api_schedule_a_ingester.main'), \
             patch('ingesters.api_schedule_b_ingester.main'), \
             patch('ingesters.api_schedule_e_ingester.main'), \
             patch('scripts.run_all_ingesters.logger') as mock_logger:
            
            from scripts.run_all_ingesters import main
            main()
            
            # Verify pipeline start and end messages
            info_calls = [str(call) for call in mock_logger.info.call_args_list]
            start_calls = [call for call in info_calls if "Starting full ingestion pipeline" in call]
            end_calls = [call for call in info_calls if "All ingestion tasks complete" in call]
            
            assert len(start_calls) == 1
            assert len(end_calls) == 1

    def test_individual_ingester_start_logging(self):
        """Test that each ingester start is logged."""
        with patch('ingesters.api_candidates_ingester.run'), \
             patch('ingesters.api_committees_ingester.run'), \
             patch('ingesters.api_schedule_a_ingester.main'), \
             patch('ingesters.api_schedule_b_ingester.main'), \
             patch('ingesters.api_schedule_e_ingester.main'), \
             patch('scripts.run_all_ingesters.logger') as mock_logger:
            
            from scripts.run_all_ingesters import main
            main()
            
            # Verify each ingester start is logged
            info_calls = [str(call) for call in mock_logger.info.call_args_list]
            
            ingester_starts = [
                "Starting Candidates Ingester",
                "Starting Committees Ingester", 
                "Starting Schedule A Ingester",
                "Starting Schedule B Ingester",
                "Starting Schedule E Ingester"
            ]
            
            for expected_msg in ingester_starts:
                matching_calls = [call for call in info_calls if expected_msg in call]
                assert len(matching_calls) == 1, f"Expected exactly one call for '{expected_msg}'"

    def test_exception_handling_continues_execution(self):
        """Test that exceptions in one ingester don't stop others."""
        call_count = {'count': 0}
        
        def count_calls(*args, **kwargs):
            call_count['count'] += 1
            if call_count['count'] == 2:  # Second call (committees) fails
                raise Exception("Committees failed")
        
        with patch('ingesters.api_candidates_ingester.run'), \
             patch('ingesters.api_committees_ingester.run', side_effect=count_calls), \
             patch('ingesters.api_schedule_a_ingester.main') as mock_schedule_a, \
             patch('ingesters.api_schedule_b_ingester.main') as mock_schedule_b, \
             patch('ingesters.api_schedule_e_ingester.main') as mock_schedule_e:
            
            from scripts.run_all_ingesters import main
            main()
            
            # Verify remaining ingesters were still called
            mock_schedule_a.assert_called_once()
            mock_schedule_b.assert_called_once()
            mock_schedule_e.assert_called_once()

class TestRunAllIngestersRobustness:
    """Test robustness and edge cases."""
    
    def test_import_errors(self):
        """Test handling of import errors."""
        with patch('ingesters.api_candidates_ingester.run', side_effect=ImportError("Module not found")), \
             patch('ingesters.api_committees_ingester.run'), \
             patch('ingesters.api_schedule_a_ingester.main'), \
             patch('ingesters.api_schedule_b_ingester.main'), \
             patch('ingesters.api_schedule_e_ingester.main'):
            
            from scripts.run_all_ingesters import main
            
            # Should not raise an exception
            main()

    def test_different_exception_types(self):
        """Test handling of different exception types."""
        with patch('ingesters.api_candidates_ingester.run', side_effect=ValueError("Invalid value")), \
             patch('ingesters.api_committees_ingester.run', side_effect=ConnectionError("Network error")), \
             patch('ingesters.api_schedule_a_ingester.main', side_effect=KeyError("Missing key")), \
             patch('ingesters.api_schedule_b_ingester.main', side_effect=TypeError("Type mismatch")), \
             patch('ingesters.api_schedule_e_ingester.main', side_effect=RuntimeError("Runtime issue")):
            
            from scripts.run_all_ingesters import main
            
            # Should handle all different exception types gracefully
            main()

    def test_none_return_values(self):
        """Test that None return values are handled correctly."""
        with patch('ingesters.api_candidates_ingester.run', return_value=None), \
             patch('ingesters.api_committees_ingester.run', return_value=None), \
             patch('ingesters.api_schedule_a_ingester.main', return_value=None), \
             patch('ingesters.api_schedule_b_ingester.main', return_value=None), \
             patch('ingesters.api_schedule_e_ingester.main', return_value=None):
            
            from scripts.run_all_ingesters import main
            
            # Should complete without issues
            main()

if __name__ == '__main__':
    pytest.main([__file__])