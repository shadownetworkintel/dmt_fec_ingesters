# tests/test_alerting.py
import pytest
from unittest.mock import patch, MagicMock
import requests
from requests.exceptions import RequestException, Timeout
import json

class TestSendSlackAlert:
    
    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/test')
    @patch('core.alerting.requests.post')
    def test_send_slack_alert_success(self, mock_post):
        """Test successful Slack alert sending."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        from core.alerting import send_slack_alert
        
        # Should not raise any exception
        send_slack_alert("Test message")
        
        # Check the call was made correctly
        mock_post.assert_called_once_with(
            'https://hooks.slack.com/test',
            json={'text': 'Test message'}
        )

    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/test')
    @patch('core.alerting.requests.post')
    def test_send_slack_alert_http_error(self, mock_post, capsys):
        """Test handling of HTTP errors."""
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response
        
        from core.alerting import send_slack_alert
        
        send_slack_alert("Test message")
        
        # Check that error was printed
        captured = capsys.readouterr()
        assert "Slack alert failed: Bad Request" in captured.out

    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/test')
    @patch('core.alerting.requests.post')
    def test_send_slack_alert_request_exception(self, mock_post):
        """Test handling of request exceptions."""
        mock_post.side_effect = RequestException("Network error")
        
        from core.alerting import send_slack_alert
        
        # Your current implementation doesn't handle exceptions
        with pytest.raises(RequestException):
            send_slack_alert("Test message")

    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/test')
    @patch('core.alerting.requests.post')
    def test_send_slack_alert_timeout(self, mock_post):
        """Test handling of timeout errors."""
        mock_post.side_effect = Timeout("Request timed out")
        
        from core.alerting import send_slack_alert
        
        # Your current implementation doesn't handle exceptions
        with pytest.raises(Timeout):
            send_slack_alert("Test message")

    @patch('core.alerting.SLACK_WEBHOOK', None)
    @patch('core.alerting.requests.post')
    def test_send_slack_alert_no_webhook(self, mock_post, capsys):
        """Test behavior when webhook URL is not configured."""
        from core.alerting import send_slack_alert
        
        send_slack_alert("Test message")
        
        # Should not make any HTTP request
        mock_post.assert_not_called()
        
        # Should print configuration message
        captured = capsys.readouterr()
        assert "Slack webhook not configured." in captured.out

    @patch('core.alerting.SLACK_WEBHOOK', '')
    @patch('core.alerting.requests.post')
    def test_send_slack_alert_empty_webhook(self, mock_post, capsys):
        """Test behavior when webhook URL is empty."""
        from core.alerting import send_slack_alert
        
        send_slack_alert("Test message")
        
        # Should not make any HTTP request
        mock_post.assert_not_called()
        
        # Should print configuration message
        captured = capsys.readouterr()
        assert "Slack webhook not configured." in captured.out

    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/test')
    @patch('core.alerting.requests.post')
    def test_send_slack_alert_empty_message(self, mock_post):
        """Test sending empty message."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        from core.alerting import send_slack_alert
        
        send_slack_alert("")
        
        # Check that empty message is sent
        mock_post.assert_called_once_with(
            'https://hooks.slack.com/test',
            json={'text': ''}
        )

    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/test')
    @patch('core.alerting.requests.post')
    def test_send_slack_alert_special_characters(self, mock_post):
        """Test sending message with special characters."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        from core.alerting import send_slack_alert
        
        special_message = "Alert! 🚨 Database error: \"Connection failed\" & retries exhausted"
        send_slack_alert(special_message)
        
        # Check that special characters are handled properly
        mock_post.assert_called_once_with(
            'https://hooks.slack.com/test',
            json={'text': special_message}
        )

    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/test')
    @patch('core.alerting.requests.post')
    def test_send_slack_alert_long_message(self, mock_post):
        """Test sending very long message."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        from core.alerting import send_slack_alert
        
        long_message = "A" * 4000  # Very long message
        send_slack_alert(long_message)
        
        # Check that long message is sent
        mock_post.assert_called_once_with(
            'https://hooks.slack.com/test',
            json={'text': long_message}
        )

    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/test')
    @patch('core.alerting.requests.post')
    def test_send_slack_alert_multiple_calls(self, mock_post):
        """Test multiple alert calls."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        from core.alerting import send_slack_alert
        
        send_slack_alert("Message 1")
        send_slack_alert("Message 2")
        send_slack_alert("Message 3")
        
        # Check all calls were made
        assert mock_post.call_count == 3
        
        # Check each call
        calls = mock_post.call_args_list
        assert calls[0][1]['json'] == {'text': 'Message 1'}
        assert calls[1][1]['json'] == {'text': 'Message 2'}
        assert calls[2][1]['json'] == {'text': 'Message 3'}

class TestSlackAlertIntegration:
    """Integration-style tests for alert functionality."""
    
    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/database-alerts')
    @patch('core.alerting.requests.post')
    def test_alert_database_error(self, mock_post):
        """Test alerting for database errors."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        from core.alerting import send_slack_alert
        
        error_msg = "🚨 Database connection failed during schedule_a ingestion"
        send_slack_alert(error_msg)
        
        # Verify the alert was sent correctly
        mock_post.assert_called_once_with(
            'https://hooks.slack.com/database-alerts',
            json={'text': error_msg}
        )

    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/ingestion-status')
    @patch('core.alerting.requests.post')
    def test_alert_ingestion_success(self, mock_post):
        """Test alerting for successful ingestion."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        from core.alerting import send_slack_alert
        
        success_msg = "✅ Schedule A ingestion completed: 1,500 records processed"
        send_slack_alert(success_msg)
        
        # Verify the alert was sent correctly
        mock_post.assert_called_once_with(
            'https://hooks.slack.com/ingestion-status',
            json={'text': success_msg}
        )

    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/api-alerts')
    @patch('core.alerting.requests.post')
    def test_alert_api_error(self, mock_post):
        """Test alerting for API errors."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        from core.alerting import send_slack_alert
        
        api_error_msg = "⚠️ FEC API rate limit exceeded, retrying in 60 seconds"
        send_slack_alert(api_error_msg)
        
        # Verify the alert was sent correctly
        mock_post.assert_called_once_with(
            'https://hooks.slack.com/api-alerts',
            json={'text': api_error_msg}
        )

    @patch('core.alerting.SLACK_WEBHOOK', 'https://hooks.slack.com/test')
    @patch('core.alerting.requests.post')
    def test_alert_with_http_errors(self, mock_post, capsys):
        """Test alert behavior with various HTTP errors."""
        from core.alerting import send_slack_alert
        
        error_codes = [400, 401, 403, 404, 500, 502, 503]
        
        for status_code in error_codes:
            mock_post.reset_mock()
            mock_response = MagicMock()
            mock_response.status_code = status_code
            mock_response.text = f"HTTP {status_code} Error"
            mock_post.return_value = mock_response
            
            send_slack_alert(f"Test message for {status_code}")
            
            # Check that error was handled
            captured = capsys.readouterr()
            assert f"Slack alert failed: HTTP {status_code} Error" in captured.out