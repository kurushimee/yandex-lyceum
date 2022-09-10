from math import inf


n = int(input())

points = []
for _ in range(n):
    s = input()
    points.append((int(s.split()[0]), (int(s.split()[1]))))

left = (inf, 0)
right = (-inf, 0)
top = (0, -inf)
bottom = (0, inf)
for point in points:
    x = point[0]
    y = point[1]
    if x > 0:
        if y < x and y > -x:
            print(point)
    else:
        if y > x and y < -x:
            print(point)

    if x < left[0]:
        left = point
    if x > right[0]:
        right = point
    if y > top[1]:
        top = point
    if y < bottom[1]:
        bottom = point

print(f"left: {left}")
print(f"right: {right}")
print(f"top: {top}")
print(f"bottom: {bottom}")
