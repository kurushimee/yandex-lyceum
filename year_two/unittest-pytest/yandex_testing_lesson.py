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


class Rectangle:
    def __init__(self, width: int | float, height: int | float):
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

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
