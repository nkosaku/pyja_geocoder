"""
pyja_geocoder package

Exposed functions:
- reverse_geocode_from_df: Vectorized reverse geocoding for a DataFrame.
- reverse_geocode_from_points: Reverse geocoding for a list of (lat, lon) tuples.
- reverse_geocode_single: Reverse geocoding for a single point.
"""

__all__ = [
    "reverse_geocode_from_df",
    "reverse_geocode_from_points",
    "reverse_geocode_single",
    "reverse_geocode_from_gdf",
    "load_japan_shapefile",
    "delete_cache",
]

from .geocode import (
    reverse_geocode_from_df,
    reverse_geocode_from_points,
    reverse_geocode_single,
    reverse_geocode_from_gdf,
    delete_cache,
)
from .data_fetcher import load_japan_shapefile
