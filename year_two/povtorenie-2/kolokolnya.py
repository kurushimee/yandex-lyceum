class BellTower:
    def __init__(self, *towers):
        self.towers = list(towers)

    def append(self, tower):
        self.towers.append(tower)

    def sound(self):
        for tower in self.towers:
            tower.sound()
        print("...")


class LittleBell:
    @staticmethod
    def sound():
        print("ding")


class BigBell:
    def __init__(self):
        self.dong = False

    def sound(self):
        if self.dong:
            print("dong")
        else:
            print("ding")
        self.dong = ~self.dong
