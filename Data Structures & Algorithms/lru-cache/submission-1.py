class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value = self.cache[key]

        # mark as most recently used
        del self.cache[key]
        self.cache[key] = value

        return value

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            # remove least recently used
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]

