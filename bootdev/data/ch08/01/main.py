class Trie:
    def add(self, word):
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
