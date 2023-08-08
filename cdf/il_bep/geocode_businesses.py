"""
Script to geocode BEP-certified businesses and write result to file
"""

import pandas as pd
from pathlib import Path
from utils.geocoding import geocode_addresses
from utils.cache import LocalFileCache
from constants import SAMPLE_BEP_CERTS_FPATH, CACHE_GEOCODED_FPATH, GEOCODED_SAMPLE_BEP_FPATH

# Define categories
categories = ['MBE', 'WBE', 'WMBE', 'SDVOSB', 'VBE', 'VOSB', 'BEPD', 'PBE', 'SWS']

# Read in raw dataset of BEP-certified businesses
df = pd.read_csv(SAMPLE_BEP_CERTS_FPATH)

# Create cache for stored geocoded addresses
cache_fpath = Path(CACHE_GEOCODED_FPATH)
cache = LocalFileCache(cache_fpath)

# Geocode addresses
street_addresses = df['Address'].tolist()
df[['Latitude', 'Longitude']] = geocode_addresses(street_addresses, cache)

# Subset to final set of columns
df[[
    "Company Name",
    "Certification Type",
    "Latitude",
    "Longitude"
]].to_csv(GEOCODED_SAMPLE_BEP_FPATH, index=False)
