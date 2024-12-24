class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
        if self.current_load() >= 0.05:
            new_hashmap = [None for i in range(len(self.hashmap) * 10)]
            old_hashmap = self.hashmap
            self.hashmap = new_hashmap
            for bucket in old_hashmap:
                if bucket != None:
                    key, value = bucket
                    self.insert(key, value)


    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        filled_buckets = 0
        for buckets in self.hashmap:
            if buckets != None:
                filled_buckets += 1
        return filled_buckets / len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
