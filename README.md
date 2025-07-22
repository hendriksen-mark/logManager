# logManager

A thread-safe logging manager for Python applications that provides easy configuration and management of multiple loggers with automatic log file naming.

## Features

- Thread-safe logger management
- Configurable log levels
- Separate handlers for stdout (DEBUG, INFO) and stderr (WARNING, ERROR, CRITICAL)
- **Automatic log file naming based on the main script name**
- Optional rolling file logging with configurable size and backup count
- Custom log file path support
- Easy integration with existing Python projects
- Utility function for hex string formatting

## Installation

### Install from GitHub (Latest)

```bash
pip install git+https://github.com/hendriksen-mark/logManager.git
```

### Install Specific Version

```bash
# Install a specific release
pip install git+https://github.com/hendriksen-mark/logManager.git@v1.0.2

# Install from a specific branch
pip install git+https://github.com/hendriksen-mark/logManager.git@main
```

### Add to requirements.txt

```
# Latest version
git+https://github.com/hendriksen-mark/logManager.git

# Specific version (recommended for production)
git+https://github.com/hendriksen-mark/logManager.git@v1.0.2
```

### Using with Poetry

```bash
poetry add git+https://github.com/hendriksen-mark/logManager.git
```

Or in `pyproject.toml`:
```toml
[tool.poetry.dependencies]
logManager = {git = "https://github.com/hendriksen-mark/logManager.git", tag = "v1.0.2"}
```

## Usage

### Basic Usage (Console logging only)

```python
from logManager.logger import Logger

# Create logger instance
logger_manager = Logger()

# Configure the logging level
logger_manager.configure_logger('DEBUG')

# Get a logger instance
my_logger = logger_manager.get_logger('my_app')

# Use the logger
my_logger.info('This is an info message')
my_logger.warning('This is a warning message')
my_logger.error('This is an error message')
```

### With Automatic File Logging

```python
from logManager.logger import Logger

# Create logger instance
logger_manager = Logger()

# Enable file logging (creates log file with same name as your script)
# If your script is "my_app.py", log file will be "my_app.log"
logger_manager.enable_file_logging(use_rolling=True)

# Configure the logging level
logger_manager.configure_logger('DEBUG')

# Get a logger instance
my_logger = logger_manager.get_logger('my_app')

# Use the logger
my_logger.info('This message will appear in console AND log file')
```

### With Custom Log File Path

```python
from logManager.logger import Logger

# Create logger with custom log file path
logger_manager = Logger(log_file_path='/path/to/custom/logfile.log')

# Or set it later
logger_manager.set_log_file_path('/path/to/another/logfile.log')

# Enable file logging
logger_manager.enable_file_logging(use_rolling=True)
```

### Check Current Configuration

```python
# Check current log level
print(f"Current log level: {logger_manager.get_level_name()}")

# Check where log file will be created
print(f"Log file path: {logger_manager._get_log_file_path()}")

# Use the hex string utility
data = bytearray([0x48, 0x65, 0x6c, 0x6c, 0x6f])
hex_string = Logger.hexstr(data)
print(f"Hex representation: {hex_string}")
```

## License

MIT License
