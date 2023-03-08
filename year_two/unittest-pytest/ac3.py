import pytest
from yandex_testing_lesson import count_chars


class Test_CountChars:
    def test_empty(self):
        assert len(count_chars("")) == 0

    def test_single(self):
        result = count_chars("a")
        assert len(result) == 1 and result["a"] == 1

    def test_no_repeating(self):
        result = count_chars("cat")
        assert (
            len(result) == 3
            and result["c"] == 1
            and result["a"] == 1
            and result["t"] == 1
        )

    def test_some_repeating(self):
        result = count_chars("door")
        assert (
            len(result) == 3
            and result["d"] == 1
            and result["o"] == 2
            and result["r"] == 1
        )

    def test_all_repeating(self):
        result = count_chars("dood")
        assert len(result) == 2 and result["d"] == 2 and result["o"] == 2

    def test_wrong_type_noniter(self):
        with pytest.raises(TypeError):
            count_chars(42)

    def test_wrong_type_iter(self):
        with pytest.raises(TypeError):
            count_chars(["s", "t", "r"])
