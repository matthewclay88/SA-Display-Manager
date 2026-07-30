"""
SA Display Manager
settings.py

Application-wide configuration values.
These are the only values that should normally be edited
when adding new dashboards or changing defaults.
"""

# -------------------------------------------------------------------
# Application Information
# -------------------------------------------------------------------

APP_NAME = "SA Display Manager"
APP_VERSION = "1.0.0"

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

DEFAULT_WHITEBOARD = r"Z:\SA_Display\whiteboard.php"

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

    "Recreation":
        "https://matthewclay88.github.io/dss-dashboard-tv/recreation.html",
}

# -------------------------------------------------------------------
# Default Dashboards
#
# These are enabled when the user clicks "Restore Defaults."
# -------------------------------------------------------------------

DEFAULT_ENABLED = [
    "DSS Dashboard",
    "Calendar",
    "Recreation",
]
