import pygame
import sys
from utils import load_image
from levels import generate_level, load_level
import numpy as np

FPS = 60
WIDTH = 640
HEIGHT = 480

player = None

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = [
        "Перемещение героя",
        "",
        "Герой двигается",
        "Карта на месте",
    ]

    background = pygame.transform.scale(
        load_image("background.jpg"), (WIDTH, HEIGHT)
    )
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color("black"))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif (
                event.type == pygame.KEYDOWN
                or event.type == pygame.MOUSEBUTTONDOWN
            ):
                return
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Перемещение героя")
    size = width, height = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    start_screen()

    player, level_x, level_y = generate_level(
        all_sprites, tiles_group, player_group, load_level("map.txt")
    )
    while True:
        x = y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 1
                if event.key == pygame.K_DOWN:
                    y += 1
                if event.key == pygame.K_LEFT:
                    x -= 1
                if event.key == pygame.K_RIGHT:
                    x += 1

        pos = (x, y)
        new_pos = tuple(np.add((player.x, player.y), pos))
        check_bounds = (0, 0) <= new_pos < (level_x, level_y)
        if check_bounds:
            check_collision = True
            for tile in tiles_group:
                if (tile.x, tile.y) == new_pos and tile.tile_type == "wall":
                    check_collision = False
                    break
            if check_collision:
                player.x += x
                player.y += y

        all_sprites.draw(screen)
        player_group.update()
        pygame.display.flip()
        clock.tick(FPS)
