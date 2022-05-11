def rhymes():
    text = [[v for v in w if v in "ауоиэыяюеё"] for w in input().split()]
    prev = text[0]
    for i in text:
        if len(i) != len(prev):
            print("Пам парам")
            return
        prev = i
    print("Парам пам-пам")


rhymes()
