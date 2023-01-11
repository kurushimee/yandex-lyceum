receipt = 1
items = []


def add_item(item_name, item_cost):
    items.append((item_name, item_cost))


def print_receipt():
    global receipt
    global items
    result = 0
    if len(items) > 0:
        print(f"Чек {receipt}. Всего предметов: {len(items)}")
        for item in items:
            print(item[0], "-", item[1])
            result += item[1]
        print(f"Итого: {result}\n-----")
        receipt += 1
        items = []
