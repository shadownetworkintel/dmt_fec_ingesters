import logging
import os
from logging.handlers import RotatingFileHandler

# Keep track of configured loggers
_configured_loggers = set()

def get_logger(name: str = "ingesters_logger") -> logging.Logger:
    logger = logging.getLogger(name)
    
    # If this logger is already configured, return it
    if name in _configured_loggers:
        return logger
        
    logger.setLevel(logging.INFO)
    
    # Clear any existing handlers for this logger
    logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Optional file logging
    log_to_file = os.getenv("LOG_TO_FILE", "false").lower() == "true"
    
    if log_to_file:
        logs_dir = "logs"
        os.makedirs(logs_dir, exist_ok=True)
        
        log_filename = os.path.join(logs_dir, "ingestion.log")

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

    # Add handlers to THIS logger (not root logger)
    logger.addHandler(console_handler)
    if file_handler:
        logger.addHandler(file_handler)
    
    # Prevent propagation to root logger to avoid duplicate messages
    logger.propagate = False
    
    # Mark this logger as configured
    _configured_loggers.add(name)

    return logger
