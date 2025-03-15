import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir="log"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO, #capture all log levels - INFO, WARNING, ERROR, and CRITICAL logs (but not DEBUG).
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # Save logs to a file
        logging.StreamHandler(sys.stdout) # Print logs to the console
    ]
)

logger = logging.getLogger("mlProjectLogger") #use to log messages