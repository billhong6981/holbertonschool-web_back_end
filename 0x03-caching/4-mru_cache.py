#!/usr/bin/python3
"""MRUCache class"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class inherit from BaseCaching"""

    def __init__(self):
        """initialize"""
        self.count = 0
        self.most_use_key = ''
        self.key_tracker = {}
        super().__init__()

    def most_recent_use_key(self):
        """Most recent use tracker"""
        l = [x for x in self.key_tracker.keys()]
        self.most_use_key = l[0]
        most_use = self.key_tracker.get(self.most_use_key)
        for x in l:
            recent_use = self.key_tracker.get(x)
            if recent_use > most_use:
                most_use = recent_use
                self.most_use_key = x
        return self.most_use_key

    def get(self, key):
        """ Get an item by key and update Most recent use index
        """
        if key is None or key not in self.cache_data.keys():
            return
        self.count += 1
        self.key_tracker.update({key: self.count})
        return self.cache_data.get(key)

    def put(self, key, item):
        """ Add an item in the cache according MRU Algorithm
        """
        if key is None or item is None:
            return
        if key in self.key_tracker.keys():
            self.key_tracker.pop(key)
        if len(self.key_tracker) >= BaseCaching.MAX_ITEMS:
            x = self.most_recent_use_key()
            print("DISCARD: {}".format(x))
            self.key_tracker.pop(x)
            self.cache_data.pop(x)
        self.cache_data.update({key: item})
        self.key_tracker.update({key: self.count})
        self.count += 1
