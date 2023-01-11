class Selector:
    def __init__(self, numbers):
        self.numbers = numbers[:]

    def get_odds(self):
        return [x for x in self.numbers if x % 2 != 0]

    def get_evens(self):
        return [x for x in self.numbers if x % 2 == 0]

