from dataclasses import dataclass


@dataclass
class Ball:
    x: int
    y: int
    radius: int


def collide_circle(first: Ball, second: Ball):
    collides_x = first.x + first.radius > second.x - second.radius
    collides_y = first.y + first.radius > second.y - second.radius
    if collides_x and collides_y:
        return "YES"
    return "NO"


c1, c2 = [Ball(*tuple(int(x) for x in input().split())) for _ in range(2)]
print(collide_circle(c1, c2))
