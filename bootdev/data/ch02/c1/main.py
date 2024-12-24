from stack import Stack


class DebounceStack(Stack):
    def push(self, item):
        if not self.items or item != self.items[-1]:
            super().push(item)
