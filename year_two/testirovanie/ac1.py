from yandex_testing_lesson import is_palindrome


def test_is_palindrome() -> str:
    test_data = (
        ('', True),
        ('a', True),
        ('aba', True),
        ('abc', False),
    )

    for input_data, expected_output in test_data:
        output = is_palindrome(input_data)
        if output != expected_output:
            return "NO"
    return "YES"


print(test_is_palindrome())
