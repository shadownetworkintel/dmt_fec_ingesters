import logging
import os
from logging.handlers import RotatingFileHandler

def get_logger(name: str = "campaign_logger") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger  # Avoid duplicate handlers

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Optional file logging
    log_to_file = os.getenv("LOG_TO_FILE", "false").lower() == "true"
    if log_to_file:
        logs_dir = "logs"
        os.makedirs(logs_dir, exist_ok=True)
        
        # One log file per logger name
        log_filename = os.path.join(logs_dir, f"{name}.log")

        # Rotate when file hits 5MB, keep 5 backups
        file_handler = RotatingFileHandler(
            log_filename, maxBytes=5_000_000, backupCount=5
        )
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
