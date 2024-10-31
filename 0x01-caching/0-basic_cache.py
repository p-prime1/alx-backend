#!/usr/bin/env python3
"""Module contains BasicCache class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Child class that inherits from BasicCaching"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves the item associated with key"""
        if key is not None:
            return self.cache_data.get(key)
        return None
