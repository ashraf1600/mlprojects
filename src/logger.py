import logging
import os
from datetime import datetime

# Step 1: Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Create full path where log file will be saved
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)  # Create logs folder if not exists

# Step 3: Combine folder path + file name
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 4: Configure logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# Test log
if __name__ == "__main__":
    logging.info("Logging has started successfully.")
