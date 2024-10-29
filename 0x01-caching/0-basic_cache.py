#!/usr/bin/env python3
BaseCaching = __import__('base_caching').BaseCaching
"""Module contains BasicCache class"""


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
        if key:
            return self.cache_data.get(key)
        return None
