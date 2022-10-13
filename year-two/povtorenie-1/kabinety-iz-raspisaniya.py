import sys

lines = list(map(str.strip, sys.stdin))
schedule = dict()
output = list()

for line in lines:
    if line == "":
        continue
    x = line.split()
    if not x[-1].isdecimal():
        continue

    index = int(x[-1])
    item = " ".join(x[:-1])
    if index not in schedule:
        schedule[index] = []
    if item not in schedule[index]:
        schedule[index].append(item)

for k, v in sorted(schedule.items()):
    output.append(f'{k}: {", ".join(v)}')
print("\n".join(output))
