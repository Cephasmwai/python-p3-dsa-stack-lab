class Stack:

    def __init__(self, items=None, limit=100):
        self.items = items[:] if items else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        if target in self.items:
            # Return how many pops from top to reach target
            return self.size() - 1 - self.items.index(target)
        return -1