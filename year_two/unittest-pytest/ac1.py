import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_single(self):
        self.assertEqual(reverse('a'), 'a')

    def test_palindrome(self):
        self.assertEqual(reverse('abba'), 'abba')

    def test_not_palindrome(self):
        self.assertEqual(reverse('abb'), 'bba')

    def test_wrong_type_noniter(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_iter(self):
        with self.assertRaises(TypeError):
            reverse(["s", "t", "r"])


if __name__ == '__main__':
     unittest.main()
