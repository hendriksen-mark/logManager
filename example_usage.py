#!/usr/bin/env python3
"""
Example usage of the updated Logger class.
This demonstrates how the logger now automatically creates log files
based on the main script name.
"""

import logging
import logManager

# Create a logger instance - it will automatically detect the main script name
logManager.logger.enable_file_logging()

# Enable file logging (this will create example_usage.log in the same directory)
logManager.logger.configure_logger('DEBUG')

 # Get a logger for this module
logger: logging.Logger = logManager.logger.get_logger(__name__)

def main():
    
    # Test different log levels
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    print(f"Current log level: {logManager.logger.get_level_name()}")
    print(f"Log file will be created at: {logManager.logger._get_log_file_path()}")

if __name__ == "__main__":
    main()
