import logging
import sys

from ingesters import (
    candidates_ingester,
    committees_ingester,
    schedule_a_ingester,
    schedule_b_ingester,
    kref_scraper,
    congress_scraper,
)
from core.logger import setup_logger

logger = setup_logger("run_all")

def run_with_logging(name, func):
    logger.info(f"Starting {name}...")
    try:
        func()
        logger.info(f"{name} completed successfully.")
    except Exception as e:
        logger.exception(f"{name} failed: {e}")

def main():
    logger.info("=== Starting full ingestion pipeline ===")

    run_with_logging("Candidates Ingester", candidates_ingester.run)
    run_with_logging("Committees Ingester", committees_ingester.run)
    run_with_logging("Schedule A Ingester", schedule_a_ingester.run)
    run_with_logging("Schedule B Ingester", schedule_b_ingester.run)
    run_with_logging("KREF Scraper", kref_scraper.run)
    run_with_logging("Congress Scraper", congress_scraper.run)

    logger.info("=== All ingestion tasks complete ===")

if __name__ == "__main__":
    main()
