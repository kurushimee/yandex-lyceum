from yandex_testing_lesson import is_prime


def test_is_prime() -> str:
    test_data = (
        ("abc", None),
        (2, True),
        (4, False),
        (3, True),
        (9, False),
        (97, True),
        (-7, None),
        (0, None),
        (1, None),
    )

    for input_data, expected_output in test_data:
        try:
            output = is_prime(input_data)
        except TypeError as e:
            if expected_output is None:
                continue
            if type(input_data) == int:
                return "NO"
        except ValueError as e:
            if expected_output is None:
                continue
            if input_data > 0:
                return "NO"
        except Exception as e:
            return "NO"
        else:
            if output != expected_output:
                return "NO"
    return "YES"


print(test_is_prime())
