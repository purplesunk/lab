class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = list(current.keys())
            if self.end_symbol in children:
                break
            if len(children) != 1:
                break
            else:
                prefix = prefix + children[0]
                current = current[children[0]]
        return prefix


    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
