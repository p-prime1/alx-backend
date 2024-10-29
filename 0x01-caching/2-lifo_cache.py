#!/usr/bin/env python
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict
"""Module contains FIFOCache class"""


class LIFOCache(BaseCaching):
    """Child class that inherits from BasicCaching"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                pop_item = self.cache_data.popitem(last=True)
                print(f"DISCARD: {pop_item[0]}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves the item associated with key"""
        if key:
            return self.cache_data.get(key)
        return None
