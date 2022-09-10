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
        kwargs = list()
        for k,v in self.kwargs:
            kwargs.append(f"{k}: {v}")



class LittleBell(Bell):
    @staticmethod
    def sound():
        print("ding")


class BigBell(Bell):
    def __init__(self):
        self.dong = False

    def sound(self):
        if self.dong:
            print("dong")
        else:
            print("ding")
        self.dong = ~self.dong
