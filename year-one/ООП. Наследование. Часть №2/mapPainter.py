import PIL import Image


class Drawer:
    def __init__(self, draw_map, cell_size):
        self.draw_map = draw_map
        self.cell_size = cell_size
        self.colors = dict()

    def numbers(self):
        nums = list()
        for row in self.draw_map:
            for col in row:
                nums.append(col)
        nums.sort()
        return nums

    def set_color(self, number, color):
        for i in range(len(self.draw_map)):
            for j in range(len(self.draw_map[0])):
                if self.draw_map[i][j] == number:
                    self.colors[(i, j)] == color
    
    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self):
        return (len(self.draw_map), len(self.draw_map[0]))

    def draw(self):
        im = Image.new("RGB", self.size(), (0, 0, 0))

        
        return im
