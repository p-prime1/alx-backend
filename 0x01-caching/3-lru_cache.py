#!/usr/bin/env python
"""Module contains FIFOCache class"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Child class that inherits from BasicCaching"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                pop_item = self.cache_data.popitem(last=False)
                print(f"DISCARD: {pop_item[0]}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves the item associated with key"""
        self.use_count = {}
        if key:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
