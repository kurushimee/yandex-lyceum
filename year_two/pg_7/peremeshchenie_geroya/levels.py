from tiles import Tile, Player


def load_level(filename):
    filename = "data/" + filename
    with open(filename, "r") as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, "."), level_map))


def generate_level(all_sprites, tiles_group, player_group, level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ".":
                Tile(tiles_group, all_sprites, "empty", x, y)
            elif level[y][x] == "#":
                Tile(tiles_group, all_sprites, "wall", x, y)
            elif level[y][x] == "@":
                Tile(tiles_group, all_sprites, "empty", x, y)
                new_player = Player(player_group, all_sprites, x, y)
    return new_player, x, y
