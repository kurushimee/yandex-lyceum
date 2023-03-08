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
