from math import sqrt


def is_prime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i) == 0:
                return False
        return True
    return False


def check_pin(pinCode):
    a, b, c = tuple(map(int, pinCode.split("-")))
    check = [False, False, False]

    # Check if a is a prime number
    check[0] = is_prime(a)

    # Check if b is a palindrome
    if str(b)[::-1] == str(b):
        check[1] = True

    # Check if c is a power of two
    if (c & (c - 1) == 0) and c != 0:
        check[2] = True

    if all(check):
        return "Корректен"
    return "Некорректен"
