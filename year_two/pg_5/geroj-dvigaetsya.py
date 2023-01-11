import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)


class Hero(pygame.sprite.Sprite):
    image = load_image("hero.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image
        self.rect = self.image.get_rect()

    def update(self, pos: Position):
        self.rect.x = pos.x
        self.rect.y = pos.y


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Герой двигается!")
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    Hero(all_sprites)

    running = True
    pos = Position(0, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pos -= Position(0, 10)
                if event.key == pygame.K_DOWN:
                    pos += Position(0, 10)
                if event.key == pygame.K_LEFT:
                    pos -= Position(10, 0)
                if event.key == pygame.K_RIGHT:
                    pos += Position(10, 0)
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        all_sprites.update(pos)
        pygame.display.flip()

    pygame.quit()
