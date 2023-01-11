from re import match


def password_level(password):
    if len(password) < 6:
        return "Недопустимый пароль"
    if (
        match(r"^[0-9]+$", password)
        or password.lower() == password
        or password.upper() == password
    ):
        if match(
            r"^([a-zA-Zа-яА-Я]+[0-9]+)$|^([0-9]+[a-zA-Zа-яА-Я]+)$", password
        ):
            return "Слабый пароль"
        return "Ненадежный пароль"
    if match(r"^[a-zA-Zа-яА-Я]+$", password):
        return "Слабый пароль"
    return "Надежный пароль"
