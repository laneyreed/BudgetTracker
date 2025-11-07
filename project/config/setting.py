import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

# Database configuration
DATABASE_PATH = DATA_DIR / "budget_tracker.db"
DATABASE_BACKUP_DIR = DATA_DIR / "backups"

# Application settings
APP_NAME = "Personal Budget Tracker"
APP_VERSION = "1.0.0"
DEFAULT_CURRENCY = "USD"
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# User preferences (can be overridden)
DEFAULT_ACCOUNT_NAME = "Main Account"
DEFAULT_BUDGET_PERIOD = "monthly"

# Reporting settings
REPORT_ITEMS_PER_PAGE = 20
EXPORT_CSV_DELIMITER = ","
CHART_COLORS = {
    "income": "#4CAF50",
    "expense": "#F44336"
}

# Notification settings
BUDGET_WARNING_THRESHOLD = 0.80  # Alert at 80% of budget
BUDGET_ALERT_THRESHOLD = 0.95    # Critical alert at 95%

# Validation rules
MIN_TRANSACTION_AMOUNT = 0.01
MAX_TRANSACTION_AMOUNT = 1000000
MAX_DESCRIPTION_LENGTH = 500

# Feature flags (enable/disable features)
ENABLE_RECURRING_TRANSACTIONS = True
ENABLE_MULTI_CURRENCY = False
ENABLE_NOTIFICATIONS = True

# Environment-specific settings
DEBUG_MODE = os.getenv("DEBUG", "False") == "True"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)