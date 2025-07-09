# logManager

A thread-safe logging manager for Python applications that provides easy configuration and management of multiple loggers.

## Features

- Thread-safe logger management
- Configurable log levels
- Separate handlers for stdout (DEBUG, INFO) and stderr (WARNING, ERROR, CRITICAL)
- Easy integration with existing Python projects
- Utility function for hex string formatting

## Installation

You can install this package directly from the repository:

```bash
pip install git+https://github.com/yourusername/logManager.git
```

Or add it to your `requirements.txt`:

```
git+https://github.com/yourusername/logManager.git
```

## Usage

```python
from logManager import logger

# Configure the logging level
logger.configure_logger('DEBUG')

# Get a logger instance
my_logger = logger.get_logger('my_app')

# Use the logger
my_logger.info('This is an info message')
my_logger.warning('This is a warning message')
my_logger.error('This is an error message')

# Check current log level
print(f"Current log level: {logger.get_level_name()}")

# Use the hex string utility
data = bytearray([0x48, 0x65, 0x6c, 0x6c, 0x6f])
hex_string = logger.hexstr(data)
print(f"Hex representation: {hex_string}")
```

## License

MIT License
