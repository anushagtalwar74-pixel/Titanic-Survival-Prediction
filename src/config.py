from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Data Paths
RAW_DATA = BASE_DIR / "data" / "raw" / "Titanic-Dataset.csv"
PROCESSED_DATA = BASE_DIR / "data" / "processed"

# Models
MODEL_DIR = BASE_DIR / "models"

# Reports
REPORT_DIR = BASE_DIR / "reports"

# Random State
RANDOM_STATE = 42