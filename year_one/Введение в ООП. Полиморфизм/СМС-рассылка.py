class Person:
    def __init__(self, first_name, middle_name, last_name, phone_numbers):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phone_numbers = phone_numbers

    def get_phone(self):
        if "private" in self.phone_numbers:
            return self.phone_numbers["private"]

    def get_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_work_phone(self):
        if "work" in self.phone_numbers:
            return self.phone_numbers["work"]

    def get_sms_text(self):
        return (
            f"Уважаемый {self.first_name} {self.middle_name}! Примите участие "
            + "в нашем беспроигрышном конкурсе для физических лиц"
        )


class Company:
    def __init__(self, name, tp, phone_numbers, *employees):
        self.name = name
        self.tp = tp
        self.phone_numbers = phone_numbers
        self.employees = employees

    def get_phone(self):
        if "contact" in self.phone_numbers:
            return self.phone_numbers["contact"]
        for employee in self.employees:
            phone = employee.get_work_phone()
            if phone:
                return phone

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return (
            f"Для компании {self.name} есть супер предложение! Примите участие"
            + f" в нашем беспроигрышном конкурсе для {self.tp}"
        )


def send_sms(*args):
    for obj in args:
        phone = obj.get_phone()
        if phone:
            text = obj.get_sms_text()
            print(f"Отправлено СМС на номер {phone} с текстом: {text}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {obj.get_name()}")
