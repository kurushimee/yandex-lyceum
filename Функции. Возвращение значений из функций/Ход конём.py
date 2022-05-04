from string import ascii_uppercase as alpha


def cell_to_coords(cell):
    return (alpha.index(cell[0]) + 1, int(cell[1]))


def coords_to_cell(coords):
    return f"{alpha[coords[0] - 1]}{coords[1]}"


def is_in_bounds(coords):
    if 1 <= coords[0] <= 8 and 1 <= coords[1] <= 8:
        return True
    return False


def possible_turns(cell):
    cell_coords = cell_to_coords(cell)
    can_turn = []
    turns = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    for turn in turns:
        turn_to = (cell_coords[0] + turn[0], cell_coords[1] + turn[1])
        if is_in_bounds(turn_to):
            can_turn.append(coords_to_cell(turn_to))
    can_turn.sort()
    return can_turn
