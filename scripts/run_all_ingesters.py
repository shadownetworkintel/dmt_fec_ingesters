
from dotenv import load_dotenv
import os

# Load default .env first (to pick up ENV_MODE and other fallback values)
load_dotenv()

# Determine which environment file to load next
env_mode = os.getenv("ENV_MODE", "dev") # Default to 'dev' if not set
env_file = f".env.{env_mode}"

# Load the environment-specific overrides (e.g., .env.dev or .env.prod)
load_dotenv(dotenv_path=env_file, override=True)

# Import all ingesters *AFTER* environment is loaded
from ingesters import (
    api_candidates_ingester,
    api_committees_ingester,
    api_schedule_a_ingester,
    api_schedule_b_ingester,
    api_schedule_e_ingester,
    api_totals_ingester
)
from core.logger import get_logger

logger = get_logger()

def run_with_logging(name, func):
    logger.info(f"Starting {name}...")
    try:
        func()
        logger.info(f"{name} completed successfully.")
    except Exception as e:
        logger.exception(f"{name} failed: {e}")

def main():
    logger.info("=== Starting full ingestion pipeline ===")

    # run_with_logging("Candidates Ingester", api_candidates_ingester.run)
    # run_with_logging("Committees Ingester", api_committees_ingester.run)
    run_with_logging("Schedule A Ingester", api_schedule_a_ingester.main)
    run_with_logging("Schedule B Ingester", api_schedule_b_ingester.main)
    run_with_logging("Schedule E Ingester", api_schedule_e_ingester.main)
    run_with_logging("Totals Ingester", api_totals_ingester.main)

    logger.info("=== All ingestion tasks complete ===")

if __name__ == "__main__":
    main()
