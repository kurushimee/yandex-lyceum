import pytest
from yandex_testing_lesson import reverse


class Test_Reverse:
    def test_empty(self):
        assert reverse("") == ""

    def test_single(self):
        assert reverse("a") == "a"

    def test_palindrome(self):
        assert reverse("abba") == "abba"

    def test_not_palindrome(self):
        assert reverse("abb") == "bba"

    def test_wrong_type_noniter(self):
        with pytest.raises(TypeError):
            reverse(42)

    def test_wrong_type_iter(self):
        with pytest.raises(TypeError):
            reverse(["s", "t", "r"])
