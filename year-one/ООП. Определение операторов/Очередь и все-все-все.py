class Queue:
    def __init__(self, *members):
        self.queue = list(members)

    def append(self, *values):
        for value in values:
            self.queue.append(value)

    def copy(self):
        return Queue(*self.queue)

    def pop(self):
        return self.queue.pop(0)

    def extend(self, other):
        self.queue.extend(other.queue)

    def next(self):
        copy = self.copy()
        copy.pop()
        return copy

    def __add__(self, other):
        copy = self.copy()
        copy.extend(other)
        return copy

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        if self.queue == other:
            return True
        return False

    def __rshift__(self, n):
        if n > len(self.queue):
            return Queue()
        copy = self.copy()
        for _ in range(n):
            copy.pop()
        return copy

    def __str__(self):
        if len(self.queue) == 0:
            return "[]"
        string = "["
        numbers = []
        for i in self.queue:
            numbers.append(str(i))
        string += " -> ".join(numbers) + "]"
        return string

    def __next__(self):
        return self.next()
