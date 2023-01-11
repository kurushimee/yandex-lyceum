import math


def discriminant(a, b, c):
    return b**2 - 4 * a * c


def larger_root(p, q):
    x1, x2 = (-p + math.sqrt(discriminant(1, p, q))) / 2, (
        -p - math.sqrt(discriminant(1, p, q))
    ) / 2
    return max(x1, x2)


def smaller_root(p, q):
    x1, x2 = (-p + math.sqrt(discriminant(1, p, q))) / 2, (
        -p - math.sqrt(discriminant(1, p, q))
    ) / 2
    return min(x1, x2)


def main():
    p, q = float(input()), float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))
