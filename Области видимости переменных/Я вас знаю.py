name = ""


def polite_input(question):
    global name
    if name == "":
        name = input("Как вас зовут?\n")
    return input(f"{name}, {question}\n")
