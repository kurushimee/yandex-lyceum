n = int(input())
og = [input() for _ in range(n)]
m = int(input())
new = [input() for _ in range(m)]

addresses = []
for x in new:
    mx = -1
    for y in og + addresses:
        y = y[:-12]
        if len(y) >= len(x) and y[:len(x)] == x[:len(x)]:
            if len(y) == len(x):
                mx = max(mx, 0)
            else:
                mx = max(mx, int(y[len(x):]))
    if mx == -1:
        addresses.append(x + "@untitled.py")
    else:
        addresses.append(x + str(mx + 1) + "@untitled.py")

print("\n".join(addresses))
