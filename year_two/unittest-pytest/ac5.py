import pytest
from yandex_testing_lesson import Rectangle


class TestRectangle:
    def test_constructor_type_error(self):
        with pytest.raises(TypeError):
            Rectangle("a", "b")

    def test_constructor_value_error(self):
        with pytest.raises(ValueError):
            Rectangle(-1, 0)

    def test_get_area(self):
        rectangle = Rectangle(2, 3)
        assert rectangle.get_area() == 6

    def test_get_perimeter(self):
        rectangle = Rectangle(4, 5)
        assert rectangle.get_perimeter() == 18
