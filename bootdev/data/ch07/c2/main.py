class HashMap:
    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while (self.hashmap[index] != None 
               and self.hashmap[index][0] != key):
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] != None:
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        raise Exception("sorry, key not found")
            

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
