import logging
import os
from datetime import datetime

# Generate a log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path for the logs directory, placing the log file inside it
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the logs directory if it does not already exist
os.makedirs(logs_path, exist_ok=True)

# Full path to the log file, combining logs directory and log file name
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging system to write logs to the specified file
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Log file to store the logs
    format="[%(asctime)s ] - %(levelname)s - %(message)s",  # Log format
    level=logging.INFO,  # Set logging level to INFO (logs INFO, WARNING, ERROR, etc.)
)
