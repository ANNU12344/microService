import os
import logging
from logging.handlers import TimedRotatingFileHandler
from src.Domain.Constant.constant import LOG_LOCATION

# Create a custom logger with a TimedRotatingFileHandler
def create_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    log_file_path = os.path.join(LOG_LOCATION)

    # Create a TimedRotatingFileHandler
    formatter = logging.Formatter("%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s")
    
    ch = TimedRotatingFileHandler(log_file_path + '.log', when="midnight")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return logger

# Create a logger instance
app_logger = create_logger(__name__)