class Cache:
    def __init__(self, cache_size, set_size):
        self.cache_size = cache_size
        self.set_size = set_size
        self.num_sets = cache_size // set_size
        self.cache = [[] for _ in range(self.num_sets)]
        self.controlPolicy = [[] for _ in range(self.num_sets)]
        self.miss_count = 0
        self.hit_count = 0

    def map_associativeLRU(self, positions):
        for position in positions:
            set_index = position % self.num_sets
            cache_set = self.cache[set_index]
            lru_set = self.controlPolicy[set_index]

            if position in cache_set:
                lru_set.remove(position)
                lru_set.append(position)
                self.hit_count += 1
            elif len(cache_set) < self.set_size:
                cache_set.append(position)
                lru_set.append(position)
                self.miss_count += 1
            else:
                lru_position = lru_set.pop(0)
                cache_set.remove(lru_position)
                cache_set.append(position)
                lru_set.append(position)
                self.miss_count += 1

    def map_associativeFIFO(self, positions):
        for position in positions:
            set_index = position % self.num_sets
            cache_set = self.cache[set_index]
            fifo_set = self.controlPolicy[set_index]

            if position in cache_set:
                self.hit_count += 1
                continue

            elif len(cache_set) < self.set_size:
                cache_set.append(position)
                fifo_set.append(position)
                self.miss_count += 1

            else:
                fifo_position = fifo_set.pop(0)
                cache_set.remove(fifo_position)
                cache_set.append(position)
                fifo_set.append(position)
                self.miss_count += 1

    def map_associativeLFU(self, positions):
        for position in positions:
            set_index = position % self.num_sets
            cache_set = self.cache[set_index]
            usage_set = self.controlPolicy[set_index]

            if position in cache_set:
                index = cache_set.index(position)
                usage_set[index] += 1
                self.hit_count += 1

            elif len(cache_set) < self.set_size:
                cache_set.append(position)
                usage_set.append(1)
                self.miss_count += 1

            else:
                min_usage = min(usage_set)
                index = usage_set.index(min_usage)
                cache_set[index] = position
                usage_set[index] = 1
                self.miss_count += 1

    def get_miss_count(self):
        return self.miss_count

    def get_hit_count(self):
        return self.hit_count

    def print_cache(self):
        for i in range(self.num_sets):
            cache_set = self.cache[i]
            for value in cache_set:
                print(f"Set {i}: {value}")


cache = Cache(cache_size=4, set_size=4)
positions = [1, 6, 1, 11, 1, 16, 1, 21, 1, 26]
cache.map_associativeLRU(positions)
print("Miss count:", cache.get_miss_count())
print("Hit count:", cache.get_hit_count())
cache.print_cache()
