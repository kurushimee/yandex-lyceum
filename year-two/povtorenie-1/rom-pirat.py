moves = [
    ("камень", "ножницы"),
    ("камень", "ром"),
    ("ножницы", "бумага"),
    ("ножницы", "ром"),
    ("бумага", "камень"),
    ("бумага", "пират"),
    ("ром", "бумага"),
    ("ром", "пират"),
    ("пират", "камень"),
    ("пират", "ножницы"),
]

first = input()
second = input()

if first == second:
    print("ничья")
else:
    for move in moves:
        if move[0] == first and move[1] == second:
            print("первый")
            break
        elif move[0] == second and move[1] == first:
            print("второй")
            break
