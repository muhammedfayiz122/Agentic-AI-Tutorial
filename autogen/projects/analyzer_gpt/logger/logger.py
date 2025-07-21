##################################################################################
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
##################################################################################

import logging
from config.loader import Config
from datetime import datetime

config = Config()

LOG_FILE = f"{datetime.now().strftime(config["logging"]["dir"])}"

if __name__ == "__main__":
    print(LOG_FILE)
