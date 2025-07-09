from .logger import Logger

# Create a global logger instance for convenience
logger = Logger()

# Export the Logger class and the global instance
__all__ = ['Logger', 'logger']
