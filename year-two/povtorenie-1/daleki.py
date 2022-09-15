import sys

data = list(map(str.strip, sys.stdin))
daleks = 0
for line in data:
    if "далек" in line.lower():
        daleks += 1
print(daleks)
