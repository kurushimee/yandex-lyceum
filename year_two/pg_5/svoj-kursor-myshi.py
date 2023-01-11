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


class Cursor(pygame.sprite.Sprite):
    image = load_image("cursor.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Cursor.image
        self.rect = self.image.get_rect()

    def update(self, pos: tuple):
        self.rect.x = pos[0]
        self.rect.y = pos[1]


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Свой курсор мыши")
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
    all_sprites = pygame.sprite.Group()
    Cursor(all_sprites)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
            all_sprites.update(pygame.mouse.get_pos())
        pygame.display.flip()

    pygame.quit()
