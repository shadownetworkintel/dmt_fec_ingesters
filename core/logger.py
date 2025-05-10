import logging
import os
from datetime import datetime

def get_logger(name: str = "campaign_logger") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger  # Avoid duplicate handlers if already configured

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Optional file handler (disabled if LOG_TO_FILE env var is not set)
    log_to_file = os.getenv("LOG_TO_FILE", "false").lower() == "true"
    if log_to_file:
        logs_dir = "logs"
        os.makedirs(logs_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = os.path.join(logs_dir, f"log_{timestamp}.log")
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.INFO)
    else:
        file_handler = None

    # Formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    console_handler.setFormatter(formatter)
    if file_handler:
        file_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(console_handler)
    if file_handler:
        logger.addHandler(file_handler)

    return logger
