import logging
import os


LOG_DIR = "reports"
LOG_FILE = os.path.join(LOG_DIR, "api_automation.log")

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("API_Automation")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)