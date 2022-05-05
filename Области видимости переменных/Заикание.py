duplicate = ""


def print_without_duplicates(message):
    global duplicate
    if message != duplicate:
        print(message)
    duplicate = message
