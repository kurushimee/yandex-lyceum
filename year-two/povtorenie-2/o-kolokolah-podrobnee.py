class BellTower:
    def __init__(self, *towers):
        self.towers = list(towers)

    def append(self, tower):
        self.towers.append(tower)

    def sound(self):
        for tower in self.towers:
            tower.sound()
        print("...")


class Bell:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def print_info(self):
        if self.args == () and self.kwargs == {}:
            print("-")
            return

        if self.kwargs != {}:
            kwargs = list()
            for k, v in self.kwargs.items():
                kwargs.append(f"{k}: {v}")
            kwargs.sort()
            print(", ".join(kwargs), end="")

            if self.args != ():
                print("; ", end="")
            else:
                print()

        if self.args != ():
            print(", ".join(self.args))


class LittleBell(Bell):
    @staticmethod
    def sound():
        print("ding")


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.dong = False

    def sound(self):
        if self.dong:
            print("dong")
        else:
            print("ding")
        self.dong = ~self.dong
