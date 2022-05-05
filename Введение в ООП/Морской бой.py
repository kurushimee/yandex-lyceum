class SeaMap:
    def __init__(self):
        self.results = dict()

    def shoot(self, row, col, result):
        self.results[(row, col)] = result
        if result == "sink":
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (row + i, col + j) not in self.results:
                        self.results[(row + i, col + j)] = "miss"
                    if self.results[(row + i, col + j)] == "hit":
                        self.shoot(row + i, col + j, result)

    def cell(self, row, col):
        output = {"miss": "*", "hit": "x", "sink": "x"}
        if (row, col) not in self.results:
            return "."
        return output[self.results[(row, col)]]
