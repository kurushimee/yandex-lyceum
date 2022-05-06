import numpy as np


class TicTacToeBoard:
    def __init__(self):
        self.new_game()

    def new_game(self):
        self.field = [["-" for _ in range(3)] for _ in range(3)]
        self.turn = True
        self.game_over = False

    def get_field(self):
        return self.field

    def check_rows(self, field):
        for row in field:
            if len(set(row)) == 1:
                return row[0]

    def check_diagonals(self, field):
        if len(set([field[i][i] for i in range(len(field))])) == 1:
            return field[0][0]
        if (
            len(set([field[i][len(field) - i - 1] for i in range(len(field))]))
            == 1
        ):
            return field[0][len(field) - 1]
        turns = list()
        for row in field:
            if "-" in row:
                turns.append(True)
        if len(turns) == 0:
            return "D"

    def check_field(self):
        for newfield in [self.field, np.transpose(self.field)]:  # type: ignore
            result = self.check_rows(newfield)
            if result and result != "-":
                return result
        result = self.check_diagonals(self.field)
        if result != "-":
            return result

    def make_move(self, row, col):
        row -= 1
        col -= 1
        if self.game_over:
            return "Игра уже завершена"
        if self.field[row][col] == "-":
            if self.turn:
                self.field[row][col] = "X"
                self.turn = not self.turn
            else:
                self.field[row][col] = "0"
                self.turn = not self.turn
        else:
            return f"Клетка {row+1}, {col+1} уже занята"
        status = self.check_field()
        if status == "X":
            self.game_over = True
            return "Победил игрок X"
        if status == "0":
            self.game_over = True
            return "Победил игрок 0"
        if status == "D":
            self.game_over = True
            return "Ничья"
        return "Продолжаем играть"
