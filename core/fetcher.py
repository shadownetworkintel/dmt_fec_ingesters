
import requests
from core.logger import get_logger
import time
import json

logger = get_logger("fetcher")

def fetch_with_retries(url, params, max_retries=10, backoff_factor=2):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=30)
            if response.status_code >= 500 or response.status_code == 429:
                raise requests.exceptions.HTTPError(f"Retryable error: {response.status_code}", response=response)
            elif response.status_code >= 400:
                # Log and bail immediately on client-side errors
                logger.error(f"Client error {response.status_code}: {response.text[:300]}")
                response.raise_for_status()
            if not response.headers.get("Content-Type", "").startswith("application/json"):
                raise ValueError(f"Expected JSON, got {response.headers.get('Content-Type')}")
            return response.json()
        except (requests.exceptions.RequestException, ValueError, json.JSONDecodeError) as e:
            wait_time = backoff_factor ** attempt
            logger.warning(f"Fetch attempt {attempt + 1}/{max_retries} failed: {e}")
            if attempt == max_retries - 1:
                logger.error("Max retries reached. Raising exception.")
                raise
            time.sleep(wait_time)