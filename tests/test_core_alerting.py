import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.alerting import send_slack_alert

send_slack_alert("Test alert from Shadow Network Intelligence 🚨")