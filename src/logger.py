import logging
import os
from datetime import datetime
import pytz  # Import pytz for timezone handling

# Define IST timezone
IST = pytz.timezone('Asia/Kolkata')

# Get current time in IST
current_time_ist = datetime.now(IST)
LOG_FILE = f"{current_time_ist.strftime('%Y-%m-%d')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]: %(levelname)s: %(message)s",
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'  # Ensure the time format is consistent
)

# Add IST timezone to log timestamps
logging.Formatter.converter = lambda *args: datetime.now(IST).timetuple()
