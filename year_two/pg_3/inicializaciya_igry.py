import pygame


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left: int, top: int, cell_size: int):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        for y, row in enumerate(self.board):
            for x, col in enumerate(row):
                left = self.left + self.cell_size * x
                top = self.top + self.cell_size * y
                pygame.draw.rect(surface, (255, 255, 255), (left, top, self.cell_size, self.cell_size), 1)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Инициализация игры')
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size)

    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
