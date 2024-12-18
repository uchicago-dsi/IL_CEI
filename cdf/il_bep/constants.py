"""Stores constant variables used throughout the application.
"""

from pathlib import Path

ROOT_DIR = Path(__file__).parents[1]
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
CACHE_DIR = DATA_DIR / "cache"
CLEAN_DIR = DATA_DIR / "clean"


SAMPLE_BEP_CERTS_FPATH = RAW_DATA_DIR / "sample_bep_certified_businesses.csv"
GEOCODED_SAMPLE_BEP_FPATH = CLEAN_DIR / "geocoded_sample_bep.csv"
CACHE_GEOCODED_FPATH = CACHE_DIR / "geocoded_addresses.json"

