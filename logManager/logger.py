import logging
import logging.handlers
import sys
import threading
from pathlib import Path
import colorlog


class Logger:
    def __init__(self, log_file_path: Path = None):
        self.loggers: dict[str, logging.Logger] = {}
        self.logLevel: int = logging.INFO  # Default to INFO level
        self._lock: threading.Lock = threading.Lock()
        self._use_rolling: bool = False  # Flag to indicate if rolling file logging is used
        self._log_file_path: Path = log_file_path  # Custom log file path

    @staticmethod
    def _get_log_format(disable_color: bool = False):
        """Return the colored log format for the logger."""
        return colorlog.ColoredFormatter(
            '%(asctime)s - %(name)s - %(lineno)d - %(log_color)s%(levelname)s - %(message)s',
            reset=True,
            log_colors={
                'DEBUG': 'cyan',
                'INFO': '',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
            no_color=disable_color
        )

    def configure_logger(self, level: str):
        """Configure the logging level for all loggers."""
        with self._lock:
            old_configured_level = logging.getLevelName(self.logLevel)
            new_level = getattr(logging, level.upper(), logging.INFO)
            
            # Only proceed if the level is actually changing
            if self.logLevel != new_level:
                self.logLevel = new_level
                changes_made: list[str] = []
                
                # Update all existing loggers with the new level
                for logger_name, logger in self.loggers.items():
                    # Clear existing handlers
                    logger.handlers.clear()
                    # Re-setup with new level
                    self._setup_logger_internal(logger_name, logger)
                    changes_made.append(f"Logger '{logger_name}' level changed from {old_configured_level} to {level.upper()}")

                if changes_made:
                    # Log the changes made to logger levels
                    return changes_made
            
            # Return None if no changes were made
            return "No changes made to logger levels"

    def _setup_logger_internal(self, name: str, logger: logging.Logger = None) -> logging.Logger:
        """Set up a logger with the given name."""
        if logger is None:
            logger = logging.getLogger(name)

        # Stream handler for stdout (DEBUG, INFO)
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(self._get_log_format())
        stdout_handler.setLevel(self.logLevel)
        stdout_handler.addFilter(lambda record: record.levelno < logging.WARNING)
        logger.addHandler(stdout_handler)

        # Stream handler for stderr (WARNING, ERROR, CRITICAL)
        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setFormatter(self._get_log_format())
        stderr_handler.setLevel(logging.WARNING)
        logger.addHandler(stderr_handler)

        # File handler for all levels
        if self._use_rolling:
            log_file_path = self._get_log_file_path()
            file_handler = logging.handlers.RotatingFileHandler(
                filename=str(log_file_path), maxBytes=10000000, backupCount=7)
            file_handler.setFormatter(self._get_log_format(True))
            file_handler.setLevel(logging.DEBUG)
            file_handler.addFilter(lambda record: record.levelno <= logging.CRITICAL)
            logger.addHandler(file_handler)

        # Set logger level to DEBUG to allow all messages through to handlers
        # Individual handlers will filter based on their own levels
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        return logger

    def get_logger(self, name):
        """Get a logger by name, creating it if necessary."""
        with self._lock:
            if name not in self.loggers:
                self.loggers[name] = self._setup_logger_internal(name)
            return self.loggers[name]

    def get_level_name(self):
        """Get the name of the current logging level."""
        return logging.getLevelName(self.logLevel)
    
    @staticmethod
    def hexstr(ba: bytearray) -> str:
        return " ".join([("0" + hex(b).replace("0x", ""))[-2:] for b in ba])

    def _get_log_file_path(self):
        """Get the log file path based on the main script name or custom path."""
        if self._log_file_path:
            return Path(self._log_file_path)
        
        # Get the main script name from sys.argv[0] or __main__ module
        try:
            import __main__
            if hasattr(__main__, '__file__') and __main__.__file__:
                main_script = Path(__main__.__file__)
                log_file_name = main_script.stem + '.log'
                return main_script.parent / log_file_name
        except (AttributeError, ImportError):
            pass
        
        # Fallback: try to get from sys.argv[0]
        if sys.argv and sys.argv[0]:
            main_script = Path(sys.argv[0])
            if main_script.suffix == '.py':
                log_file_name = main_script.stem + '.log'
                return main_script.parent / log_file_name
        
        # Final fallback: use current working directory with generic name
        return Path.cwd() / 'application.log'

    def set_log_file_path(self, log_file_path):
        """Set a custom log file path."""
        with self._lock:
            self._log_file_path = log_file_path
            # Update all existing loggers with the new file path
            for logger_name, logger in self.loggers.items():
                # Clear existing handlers
                logger.handlers.clear()
                # Re-setup with new file path
                self._setup_logger_internal(logger_name, logger)

    def enable_file_logging(self, use_rolling=True):
        """Enable file logging with optional rolling."""
        with self._lock:
            self._use_rolling = use_rolling
            # Update all existing loggers
            for logger_name, logger in self.loggers.items():
                logger.handlers.clear()
                self._setup_logger_internal(logger_name, logger)

    def disable_file_logging(self):
        """Disable file logging."""
        with self._lock:
            self._use_rolling = False
            # Update all existing loggers to remove file handlers
            for logger_name, logger in self.loggers.items():
                logger.handlers.clear()
                self._setup_logger_internal(logger_name, logger)
