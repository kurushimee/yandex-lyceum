def convert_to_roman(n):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = [
        "I",
        "IV",
        "V",
        "IX",
        "X",
        "XL",
        "L",
        "XC",
        "C",
        "CD",
        "D",
        "CM",
        "M",
    ]
    i = 12

    output = ""
    while n:
        div = n // num[i]
        n %= num[i]

        while div:
            output += sym[i]
            div -= 1
        i -= 1
    return output


one = 0
two = 0
three = ""


def roman():
    global three
    three = one + two
    print(
        f"{convert_to_roman(one)} + {convert_to_roman(two)} = ",
        f"{convert_to_roman(three)}",
    )
