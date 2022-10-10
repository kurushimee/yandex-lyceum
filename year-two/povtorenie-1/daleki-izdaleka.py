import sys

data = list(map(str.strip, sys.stdin))
daleks = 0
for line in data:
    for word in line.split():
        if "далек" in word.lower()[:5]:
            daleks += 1
            break
print(daleks)
