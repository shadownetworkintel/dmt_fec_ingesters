from core.env import load_environment

# Load environment (.env + .env.<ENV_MODE>)
load_environment()

# Import all ingesters *AFTER* environment is loaded
from ingesters import (
    api_schedule_a_ingester,
    api_schedule_b_ingester,
    api_schedule_e_ingester,
    api_candidates_ingester,
    api_committees_ingester,
    api_committees_new,
    api_candidates_new,
    api_totals_ingester,
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

    run_with_logging("Committees Ingester", api_committees_new.main)
    run_with_logging("Candidates Ingester", api_candidates_new.main)
    run_with_logging("Schedule A Ingester", api_schedule_a_ingester.main)
    run_with_logging("Schedule B Ingester", api_schedule_b_ingester.main)
    run_with_logging("Schedule E Ingester", api_schedule_e_ingester.main)
    run_with_logging("Totals Ingester", api_totals_ingester.main)
    # run_with_logging("Committees Ingester", api_committees_ingester.run)
    # run_with_logging("Candidates Ingester", api_candidates_ingester.run)

    logger.info("=== All ingestion tasks complete ===")

if __name__ == "__main__":
    main()
