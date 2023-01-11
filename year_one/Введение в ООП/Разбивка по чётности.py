class OddEvenSeparator:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def even(self):
        return [x for x in self.numbers if x % 2 == 0]

    def odd(self):
        return [x for x in self.numbers if x % 2 != 0]
