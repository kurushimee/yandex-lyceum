from math import sqrt


def roots_of_quadratic_equation(a, b, c):
    solutions = []

    if a == 0:
        if b == 0:
            if c == 0:
                solutions.append("all")
        else:
            solutions.append(-c / b)
    else:
        d = b**2 - 4 * a * c
        if d == 0:
            solutions.append(-b / (2 * a))
        elif d > 0:
            solutions.append((-b - sqrt(d)) / (2 * a))
            solutions.append((-b + sqrt(d)) / (2 * a))

    return solutions
