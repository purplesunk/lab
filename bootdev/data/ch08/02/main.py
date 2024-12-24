class Trie:
    def exists(self, word):
        current = self.root
        for c in word:
            if c not in current:
                return False
            current = current[c]
        if self.end_symbol in current:
            return True
        else:
            return False
            

    # don't touch below this line

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
