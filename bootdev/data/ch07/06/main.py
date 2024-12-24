class HashMap:
    def get(self, key):
        index = self.key_to_index(key)
        value = self.hashmap[index]
        if value == None:
            raise Exception("sorry, key not found")
        return value[1]

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
