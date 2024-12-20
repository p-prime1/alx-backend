#!/usr/bin/env python3
"""
    BaseCaching module
"""


class BaseCaching():
    """BaseCaching defines:
    - constants of the caching system
    - where data are stored (in a dictionary)
    """

    MAX_ITEMS = 4

    def __init__(self):
        """Inittialize
        """
        self.cache_data = {}

    def print_cache(self):
        """Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Addan item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
