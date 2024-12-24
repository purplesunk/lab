class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if not self.items:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
