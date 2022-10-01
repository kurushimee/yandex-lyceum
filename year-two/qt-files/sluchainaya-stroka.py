from random import randrange

with open("lines.txt", encoding="utf8") as f:
    lines = f.readlines()
    if lines != []:
        print(lines[randrange(len(lines)) - 1])
