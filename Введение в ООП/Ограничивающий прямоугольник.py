import math


class BoundingRectangle:
    def __init__(self):
        self.points = []

    def add_point(self, *coords):
        self.points.append(coords)

    def width(self):
        return int(math.sqrt((self.right_x() - self.left_x()) ** 2))

    def height(self):
        return int(math.sqrt((self.top_y() - self.bottom_y()) ** 2))

    def left_x(self):
        return min(map(lambda n: n[0], self.points))

    def right_x(self):
        return max(map(lambda n: n[0], self.points))

    def bottom_y(self):
        return min(map(lambda n: n[1], self.points))

    def top_y(self):
        return max(map(lambda n: n[1], self.points))
