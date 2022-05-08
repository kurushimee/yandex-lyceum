class Table:
    def __init__(self, rows, cols):
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            return self.table[row][col]

    def set_value(self, row, col, value):
        if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            self.table[row][col] = value

    def n_rows(self):
        return len(self.table)

    def n_cols(self):
        try:
            return len(self.table[0])
        except IndexError:
            return 0

    def delete_row(self, row):
        del self.table[row]

    def delete_col(self, col):
        for row in self.table:
            del row[col]

    def add_row(self, row):
        cols = self.n_cols()
        self.table.insert(row, [0 for _ in range(cols if cols > 0 else 1)])

    def add_col(self, col):
        for row in self.table:
            row.insert(col, 0)
