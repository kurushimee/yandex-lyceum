def collide_rectangle(first: tuple, second: tuple):
    x1, y1, w1, h1 = first
    x2, y2, w2, h2 = second
    collides_left = x1 < x2 + w2 and not x1 + w1 < x2
    collides_right = x1 + w1 > x2 and not x1 > x2 + w2
    collides_up = y1 < y2 + h2 and not y1 + h1 < y2
    collides_down = y1 + h1 > y2 and not y1 > y2 + h2
    if (collides_left or collides_right) and (collides_up or collides_down):
        return "YES"
    return "NO"


r1, r2 = tuple(tuple(map(int, input().split())) for _ in range(2))
print(collide_rectangle(r1, r2))
