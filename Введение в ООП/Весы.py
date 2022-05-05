class Balance:
    def __init__(self):
        self.left, self.right = 0, 0

    def add_left(self, x):
        self.left += x

    def add_right(self, x):
        self.right += x

    def result(self):
        if self.left > self.right:
            return "L"
        elif self.left < self.right:
            return "R"
        else:
            return "="
