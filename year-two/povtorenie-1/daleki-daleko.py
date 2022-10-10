import sys

singular = ["далек", "далека", "далеку", "далеком", "далеке"]
multiple = ["далеки", "далеков", "далекам", "далеками", "далеках"]

data = list(map(str.strip, sys.stdin))
daleks = 0
for line in data:
    str.strip(line, "()[]{},;:.?!\"\"''")
    for word in line.split():
        if word.lower() in singular or word.lower() in multiple:
            daleks += 1
            break
print(daleks)
