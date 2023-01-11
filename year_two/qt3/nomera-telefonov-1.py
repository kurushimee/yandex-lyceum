def check_number(number):
    new_number = "+7"

    if number[0] == "8":
        number = number[1:]
    elif number[:2] == "+7":
        number = number[2:]
    else:
        return "error"

    prev_char = ""
    open_parens = False
    for char in number:
        if not str.isdigit(char) and char not in "-()":
            return "error"
        if char == "-" and number.index(char) == len(number) - 1:
            return "error"
        if char == "-" and prev_char == "-":
            return "error"
        if char == "(" and open_parens:
            return "error"
        if char == ")" and not open_parens:
            return "error"
        if char == "(":
            open_parens = True
        if char == ")":
            open_parens = False
        if str.isdigit(char):
            new_number += char
        prev_char = char
    if open_parens or len(new_number) != 12:
        return "error"

    return new_number


print(check_number("".join(input().split())))
