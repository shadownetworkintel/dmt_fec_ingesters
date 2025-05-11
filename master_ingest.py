import logging
from core.logger import get_logger

# Import all your ingester modules
from ingesters import (
    api_candidates_ingester,
    api_committees_ingester,
    api_schedule_a_ingester,
    api_schedule_b_ingester,
    api_schedule_e_ingester,
    # Add more as you build them
)

logger = get_logger("master_ingest")

def run_all():
    logger.info("=== Starting master ingester ===")

    try:
        logger.info("Running candidate ingester...")
        api_candidates_ingester.run()
    except Exception as e:
        logger.exception("Candidate ingester failed.")

    try:
        logger.info("Running committee ingester...")
        api_committees_ingester.run()
    except Exception as e:
        logger.exception("Committee ingester failed.")

    try:
        logger.info("Running Schedule A ingester...")
        api_schedule_a_ingester.run()
    except Exception as e:
        logger.exception("Schedule A ingester failed.")

    try:
        logger.info("Running Schedule B ingester...")
        api_schedule_b_ingester.run()
    except Exception as e:
        logger.exception("Schedule B ingester failed.")

    try:
        logger.info("Running Schedule E ingester...")
        api_schedule_e_ingester.run()
    except Exception as e:
        logger.exception("Schedule E ingester failed.")

    logger.info("=== Master ingester finished ===")

if __name__ == "__main__":
    run_all()