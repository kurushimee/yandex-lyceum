pi = 3.14159


def circle_length(radius):
    return pi * (radius * 2)


def circle_area(radius):
    return pi * (radius**2)


def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))
