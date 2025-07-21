##################################################################################
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
##################################################################################

import logging
from config.loader import Config
from datetime import datetime
from utils.paths import ROOT_DIR

config = Config()

LOG_FILE = f"{datetime.now().strftime(config["logging"]["format"])}"
LOG_FILE_PATH = os.path.join(ROOT_DIR, config["logging"]["dir"], LOG_FILE)

os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
    level=logging.DEBUG
)

if __name__ == "__main__":
    logging.critical("testing")
