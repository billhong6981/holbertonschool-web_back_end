#!/usr/bin/python3
"""FIFOCache class"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class inherit from BaseCaching"""

    def __init__(self):
        """initialize"""
        self.key_list = []
        super().__init__()

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data.get(key)

    def put(self, key, item):
        """ Add an item in the cache whether discard or not
        """
        if key is None or item is None:
            return
        if key in self.key_list:
            self.key_list.remove(key)
        if len(self.key_list) >= BaseCaching.MAX_ITEMS:
            x = self.key_list[0]
            print("DISCARD: {}".format(x))
            self.key_list.pop(0)
            self.cache_data.pop(x)
        self.cache_data.update({key: item})
        self.key_list.append(key)
