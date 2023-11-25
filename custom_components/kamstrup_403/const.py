"""Constants for Kamstrup."""
from typing import Final

# Base component constants
NAME: Final = "Kamstrup 403"
DOMAIN: Final = "kamstrup_403"
VERSION: Final = "2.6.0"
MANUFACTURER: Final = "Kamstrup"
ATTRIBUTION: Final = "Data provided by Kamstrup meter"

# Defaults
DEFAULT_NAME: Final = "kamstrup" # Used for sensor name prefix
DEFAULT_BAUDRATE: Final = 9600
DEFAULT_SCAN_INTERVAL: Final = 60
DEFAULT_TIMEOUT: Final = 1.0
DEFAULT_DEVICE_MODEL: Final = "403"

# Device models
DEVICE_MODELS: Final = ["403", "382"]

