class Date:
    MONTHS = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        return (self.day + Date.MONTHS[self.month - 1]) - (
            other.day + Date.MONTHS[other.month - 1]
        )
