"""
Geocodes street adresses to latitute and longitude coordinates
"""

import requests
from typing import List, Tuple
from utils.cache import LocalFileCache


def geocode_addresses(
    addresses: List[str],
    cache: LocalFileCache) -> List[Tuple[float, float]]:
    """
    Geocodes a list of street addresses to latitude
    longitude coordinate pairs.
    
    Args:
        list of addresses
    
    Returns:
        list of tuples, each consisting of a latitude and a longitude coordinate 
    """
    geocoded = []
    base_url = "https://nominatim.openstreetmap.org/search"
    for address in addresses:
        
        # Check the cache to see if the address has been processed already
        coords = cache.fetch(address)
        if coords:
            lat, lon = coords
            geocoded.append((lat, lon,))
            continue
        
        # Define the API request for the address
        url = f"{base_url}?q={address}&format=json&limit=1"
        
        # Make the request with a timeout of 5 seconds
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            response_body = response.json()
            lat = float(response_body[0]['lat'])
            lon = float(response_body[0]['lon'])
            geocoded.append((lat, lon))
            cache.store(address, (lat, lon))
        except (requests.exceptions.RequestException, IndexError) as e:
            geocoded.append((None, None))

    return geocoded

        