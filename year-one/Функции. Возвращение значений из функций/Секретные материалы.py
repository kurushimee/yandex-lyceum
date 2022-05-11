def print_document(pages):
    for page in pages:
        if page.split()[0] == "Секретно":
            print("Дальнейшие материалы засекречены")
            return
        else:
            print(page)
    print("Напечатано без купюр")
