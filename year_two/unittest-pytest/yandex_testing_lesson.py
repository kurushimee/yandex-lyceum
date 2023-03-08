from typing import Dict


def reverse(s: str) -> str:
    if type(s) != str:
        raise TypeError("Expected str, got {}".format(type(s)))

    return s[::-1]


def count_chars(s: str) -> Dict[str, int]:
    if type(s) != str:
        raise TypeError("Expected str, got {}".format(type(s)))

    char_set = set(s)
    char_counts = dict()
    for char in char_set:
        char_counts[char] = s.count(char)

    return char_counts


def is_under_queen_attack(position: str, queen_position: str) -> bool:
    if type(position) != str or type(queen_position) != str:
        raise TypeError(
            "Expected str, got {} and {}".format(
                type(position), type(queen_position)
            )
        )

    valid_letters = "abcdefgh"
    valid_numbers = "12345678"
    if len(position) != 2 or len(queen_position) != 2:
        raise ValueError("Coordinates must have two characters")
    if position[0] not in valid_letters or position[1] not in valid_numbers:
        raise ValueError("Invalid coordinate: " + position)
    if (
        queen_position[0] not in valid_letters
        or queen_position[1] not in valid_numbers
    ):
        raise ValueError("Invalid coordinate: " + queen_position)

    # convert coordinates to numbers
    pos_x = ord(position[0]) - ord("a") + 1
    pos_y = int(position[1])
    queen_x = ord(queen_position[0]) - ord("a") + 1
    queen_y = int(queen_position[1])

    if pos_x == queen_x and pos_y == queen_y:
        return True

    if pos_x == queen_x or pos_y == queen_y:
        return True
    if abs(pos_x - queen_x) == abs(pos_y - queen_y):
        return True

    return False


class Rectangle:
    def __init__(self, width: int | float, height: int | float) -> None:
        acceptable_types = (int, float)
        if not (
            type(width) in acceptable_types
            and type(height) in acceptable_types
        ):
            raise TypeError(
                "Expected int or float, got {} and {}".format(
                    type(width), type(height)
                )
            )
        if width < 0 or height < 0:
            raise ValueError(
                f"Expected width and height >= 0, got {width} and {height}"
            )
        self.width = width
        self.height = height

    def get_area(self) -> int | float:
        return self.width * self.height

    def get_perimeter(self) -> int | float:
        return 2 * (self.width + self.height)
