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


class Car(pygame.sprite.Sprite):
    image = load_image("car.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Car.image
        self.rect = self.image.get_rect()

    def update(self, pos: Position, invert: bool = False):
        self.rect.x = pos.x
        self.rect.y = pos.y
        if invert:
            self.image = pygame.transform.flip(self.image, True, False)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Герой двигается!")
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    Car(all_sprites)

    running = True
    pos = Position(0, 0)
    speed = 50
    invert = False
    fps = 60
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        if not invert and pos.x >= 600 - Car.image.get_width():
            speed = -speed
            invert = True
            all_sprites.update(pos, invert=True)
        if invert and pos.x <= 0:
            speed = -speed
            invert = False
            all_sprites.update(pos, invert=True)
        pos += Position(speed / fps, 0)
        all_sprites.draw(screen)
        all_sprites.update(pos)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
