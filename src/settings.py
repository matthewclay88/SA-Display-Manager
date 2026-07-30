"""
SA Display Manager
settings.py

Application-wide configuration values.

This module defines:
- application metadata
- default slideshow settings
- supported dashboards
- default dashboard selection
- backup behavior

Most future configuration changes should only require editing this file.
"""

# -------------------------------------------------------------------
# Application Information
# -------------------------------------------------------------------

APP_NAME = "SA Display Manager"
APP_VERSION = "1.0"

# -------------------------------------------------------------------
# Default Slideshow Settings
# -------------------------------------------------------------------

DEFAULT_INTERVAL = 20  # seconds

# -------------------------------------------------------------------
# Whiteboard File
#
# This is the default location. The user will be able to browse
# to a different file from the application if necessary.
# -------------------------------------------------------------------

DEFAULT_WHITEBOARD_PATH = r"Z:\SA_Display\whiteboard.php"

# -------------------------------------------------------------------
# Supported File Types
# -------------------------------------------------------------------

SUPPORTED_EXTENSIONS = (
    ".php",
)


# -------------------------------------------------------------------
# Available Dashboards
#
# Format:
# "Display Name": "URL"
# -------------------------------------------------------------------

DASHBOARDS = {
    "DSS Dashboard":
        "https://matthewclay88.github.io/dss-dashboard-tv/",

    "Calendar":
        "https://matthewclay88.github.io/dss-dashboard-tv/calendar.html",

    "Lake Champlain Recreation":
        "https://matthewclay88.github.io/dss-dashboard-tv/recreation.html",

    "Mountain Recreation":
        "https://matthewclay88.github.io/dss-dashboard-tv/recreation_winter.html",

    "Current Products":
        "https://matthewclay88.github.io/dss-dashboard-tv/products.html",

    "Verification":
        "https://matthewclay88.github.io/dss-dashboard-tv/verification.html",
}

# -------------------------------------------------------------------
# Default Dashboards
#
# These are enabled when the user clicks "Restore Defaults."
# -------------------------------------------------------------------

DEFAULT_ENABLED = [
    "DSS Dashboard",
    "Calendar",
]

# -------------------------------------------------------------------
# Backup Settings
# -------------------------------------------------------------------

BACKUP_EXTENSION = ".bak"
