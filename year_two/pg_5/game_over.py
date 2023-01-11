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


class GameOver(pygame.sprite.Sprite):
    image = load_image("game_over.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = GameOver.image
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self):
        if self.rect.x < 0:
            self.rect = self.rect.move(200 / 60, 0)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Game over")
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    GameOver(all_sprites)

    running = True
    fps = 60
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 255))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
