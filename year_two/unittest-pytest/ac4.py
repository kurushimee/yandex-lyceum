import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_same_position():
    assert is_under_queen_attack("e2", "e2")


def test_same_row():
    assert is_under_queen_attack("a4", "h4")


def test_same_column():
    assert is_under_queen_attack("c3", "c7")


def test_diagonal():
    assert is_under_queen_attack("f5", "b1")


def test_no_attack():
    assert not is_under_queen_attack("d6", "h5")


def test_non_string_input():
    with pytest.raises(TypeError):
        is_under_queen_attack(12, "a5")
    with pytest.raises(TypeError):
        is_under_queen_attack("a5", 12)
    with pytest.raises(TypeError):
        is_under_queen_attack(12, 12)


def test_invalid_length_input():
    with pytest.raises(ValueError):
        is_under_queen_attack("abc", "d4")
    with pytest.raises(ValueError):
        is_under_queen_attack("d4", "abc")
    with pytest.raises(ValueError):
        is_under_queen_attack("abc", "abc")


def test_invalid_letter_input():
    with pytest.raises(ValueError):
        is_under_queen_attack("j5", "e3")
    with pytest.raises(ValueError):
        is_under_queen_attack("e3", "j5")
    with pytest.raises(ValueError):
        is_under_queen_attack("j5", "j5")


def test_invalid_number_input():
    with pytest.raises(ValueError):
        is_under_queen_attack("b9", "c6")
    with pytest.raises(ValueError):
        is_under_queen_attack("c6", "b9")
    with pytest.raises(ValueError):
        is_under_queen_attack("b9", "b9")
