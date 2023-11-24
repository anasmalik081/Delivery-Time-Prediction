"""
Script for logging
"""

# importing libraries
import os, sys
import logging
from datetime import datetime


# log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# log path
LOG_PATH = os.path.join(os.getcwd(), 'logs', LOG_FILE)

# making log directory
os.makedirs(LOG_PATH, exist_ok=True)

# log file path
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

# logs config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)