class BigBell:
    def __init__(self):
        self.next = "ding"

    def sound(self):
        print(self.next)
        if self.next == "ding":
            self.next = "dong"
        else:
            self.next = "ding"
