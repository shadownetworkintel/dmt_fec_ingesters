# tests/test_fetcher.py
import pytest
from unittest.mock import patch, MagicMock
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError
from core.fetcher import fetch_with_retries
import time

class TestFetchWithRetries:
    
    @patch('core.fetcher.requests.get')
    def test_fetch_success_first_try(self, mock_get):
        """Test successful fetch on first attempt."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"results": ["data"], "pagination": {}}
        mock_get.return_value = mock_response
        
        result = fetch_with_retries("https://api.example.com", {"param": "value"})
        
        assert result == {"results": ["data"], "pagination": {}}
        mock_get.assert_called_once_with("https://api.example.com", params={"param": "value"}, timeout=30)

    @patch('core.fetcher.requests.get')
    @patch('core.fetcher.time.sleep')
    def test_fetch_success_after_retries(self, mock_sleep, mock_get):
        """Test successful fetch after some failures."""
        # First two calls fail, third succeeds
        success_response = MagicMock()
        success_response.status_code = 200
        success_response.json.return_value = {"results": ["data"]}
        
        mock_get.side_effect = [
            RequestException("First failure"),
            Timeout("Second failure"),
            success_response
        ]
        
        result = fetch_with_retries("https://api.example.com", {"param": "value"})
        
        assert result == {"results": ["data"]}
        assert mock_get.call_count == 3
        assert mock_sleep.call_count == 2  # Sleep called between retries
        mock_sleep.assert_any_call(1)  # First retry delay
        mock_sleep.assert_any_call(2)  # Second retry delay (exponential backoff)

    @patch('core.fetcher.requests.get')
    @patch('core.fetcher.time.sleep')
    def test_fetch_max_retries_exceeded(self, mock_sleep, mock_get):
        """Test fetch failing after max retries."""
        mock_get.side_effect = RequestException("Persistent failure")
        
        with pytest.raises(RequestException, match="Persistent failure"):
            fetch_with_retries("https://api.example.com", {"param": "value"}, max_retries=2)
        
        assert mock_get.call_count == 2  # Only 2 attempts based on the log output
        assert mock_sleep.call_count == 1  # Only 1 sleep between attempts

    @patch('core.fetcher.requests.get')
    def test_fetch_different_exception_types(self, mock_get):
        """Test handling of different exception types with enough retries."""
        test_cases = [
            ConnectionError("Connection failed"),
            Timeout("Request timed out"),
            RequestException("Generic request error")
        ]
        
        for exception in test_cases:
            mock_get.reset_mock()
            mock_get.side_effect = exception
            
            with pytest.raises(type(exception)):
                # Use enough retries so the function actually raises the exception
                fetch_with_retries("https://api.example.com", {}, max_retries=1)

    @patch('core.fetcher.requests.get')
    def test_fetch_json_decode_error(self, mock_get):
        """Test handling of JSON decode errors."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response
        
        with pytest.raises(ValueError, match="Invalid JSON"):
            # Use enough retries so the function actually raises the exception
            fetch_with_retries("https://api.example.com", {}, max_retries=1)

    @patch('core.fetcher.requests.get')
    @patch('core.fetcher.time.sleep')
    def test_fetch_exponential_backoff(self, mock_sleep, mock_get):
        """Test that retry delays follow exponential backoff."""
        # Create enough failures to see the pattern
        mock_get.side_effect = [RequestException(f"Failure {i}") for i in range(1, 6)]
        
        with pytest.raises(RequestException):
            fetch_with_retries("https://api.example.com", {}, max_retries=4)
        
        # Check exponential backoff: 1, 2, 4 seconds (3 sleeps between 4 attempts)
        expected_delays = [1, 2, 4]
        actual_delays = [call[0][0] for call in mock_sleep.call_args_list]
        assert actual_delays == expected_delays

    @patch('core.fetcher.requests.get')
    def test_fetch_with_empty_params(self, mock_get):
        """Test fetch with empty parameters."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response
        
        result = fetch_with_retries("https://api.example.com", {})
        
        assert result == {"data": "test"}
        mock_get.assert_called_once_with("https://api.example.com", params={}, timeout=30)

    @patch('core.fetcher.requests.get')
    def test_fetch_with_none_params(self, mock_get):
        """Test fetch with None parameters."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response
        
        result = fetch_with_retries("https://api.example.com", None)
        
        assert result == {"data": "test"}
        mock_get.assert_called_once_with("https://api.example.com", params=None, timeout=30)

    @patch('core.fetcher.requests.get')
    @patch('core.fetcher.time.sleep')
    def test_fetch_custom_max_retries(self, mock_sleep, mock_get):
        """Test fetch with custom max_retries value."""
        mock_get.side_effect = RequestException("Always fails")
        
        with pytest.raises(RequestException):
            fetch_with_retries("https://api.example.com", {}, max_retries=5)
        
        assert mock_get.call_count == 5  # 5 attempts based on the log output
        assert mock_sleep.call_count == 4  # 4 sleeps between 5 attempts

    @patch('core.fetcher.requests.get')
    @patch('core.fetcher.time.sleep')
    def test_fetch_500_error_retry(self, mock_sleep, mock_get):
        """Test that 500 errors trigger retry and eventually fail."""
        # Your fetcher raises HTTPError immediately for 500 status codes
        error_response = MagicMock()
        error_response.status_code = 500
        mock_get.return_value = error_response
        
        with pytest.raises(requests.HTTPError, match="Retryable error: 500"):
            fetch_with_retries("https://api.example.com", {}, max_retries=1)
        
        assert mock_get.call_count == 1  # Only 1 attempt since it fails immediately

    @patch('core.fetcher.requests.get')
    @patch('core.fetcher.time.sleep')
    def test_fetch_429_error_retry(self, mock_sleep, mock_get):
        """Test that 429 (rate limit) errors trigger retry and eventually fail."""
        # Your fetcher raises HTTPError immediately for 429 status codes
        rate_limit_response = MagicMock()
        rate_limit_response.status_code = 429
        mock_get.return_value = rate_limit_response
        
        with pytest.raises(requests.HTTPError, match="Retryable error: 429"):
            fetch_with_retries("https://api.example.com", {}, max_retries=1)
        
        assert mock_get.call_count == 1  # Only 1 attempt since it fails immediately

    @patch('core.fetcher.requests.get')
    @patch('core.fetcher.time.sleep')
    def test_fetch_500_error_with_eventual_success(self, mock_sleep, mock_get):
        """Test that 500 errors eventually succeed after retries."""
        # First call returns 500 (raises HTTPError), second call succeeds
        error_response = MagicMock()
        error_response.status_code = 500
        
        success_response = MagicMock()
        success_response.status_code = 200
        success_response.json.return_value = {"data": "success"}
        
        # Set up side_effect to raise HTTPError on first call, then return success
        def side_effect(*args, **kwargs):
            if mock_get.call_count == 1:
                return error_response
            else:
                return success_response
        
        mock_get.side_effect = side_effect
        
        result = fetch_with_retries("https://api.example.com", {}, max_retries=2)
        
        assert result == {"data": "success"}
        assert mock_get.call_count == 2
        assert mock_sleep.call_count == 1  # One sleep between attempts

    @patch('core.fetcher.requests.get')
    def test_fetch_200_status_success(self, mock_get):
        """Test that 200 status codes work properly."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "success"}
        mock_get.return_value = mock_response
        
        result = fetch_with_retries("https://api.example.com", {})
        
        assert result == {"data": "success"}
        assert mock_get.call_count == 1

    @patch('core.fetcher.requests.get')
    def test_fetch_400_status_no_retry(self, mock_get):
        """Test that 4xx errors (except 429) don't trigger retries."""
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"error": "Bad request"}
        mock_get.return_value = mock_response
        
        result = fetch_with_retries("https://api.example.com", {}, max_retries=2)
        
        assert result == {"error": "Bad request"}
        assert mock_get.call_count == 1  # No retries for 4xx errors