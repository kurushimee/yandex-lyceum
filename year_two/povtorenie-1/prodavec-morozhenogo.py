n = int(input())
flavours = dict()
for _ in range(n):
    flavour, price = input().split("	")
    flavours[flavour] = int(price)

# Input divider
input()

orders = [[]]
while (s := input()) != ".":
    if s == "":
        orders.append([])
        continue
    flavour, amount = s.split("	")
    cost = flavours[flavour] * int(amount)
    orders[-1].append(cost)

i = 1
for order in orders:
    if order:
        print(f"{i}) {sum(order)}")
        i += 1
print(f"Итого: {sum([sum(x) for x in orders])}")
