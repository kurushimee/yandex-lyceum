from utils import load_image
import pygame

tile_images = {"wall": load_image("box.png"), "empty": load_image("grass.png")}
player_image = load_image("mario.png")

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tiles_group, all_sprites, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.tile_type = tile_type
        self.image = tile_images[self.tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y
        )
        self.x = pos_x
        self.y = pos_y


class Player(pygame.sprite.Sprite):
    def __init__(self, player_group, all_sprites, x, y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.x = x
        self.y = y
        self.change_pos()

    def update(self):
        self.change_pos()

    def change_pos(self):
        self.rect = self.image.get_rect().move(
            tile_width * self.x + 15, tile_height * self.y + 5
        )
