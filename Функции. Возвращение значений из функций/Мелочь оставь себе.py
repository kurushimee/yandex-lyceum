def take_large_banknotes(banknotes):
    can_buy_with_it = []
    for banknote in banknotes:
        if banknote > 10:
            can_buy_with_it.append(banknote)
    return can_buy_with_it
