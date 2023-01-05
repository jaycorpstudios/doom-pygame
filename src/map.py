import pygame as pg

_ = False

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, 1, 1, 1, _, _, _, _, _, _, 1],
    [1, _, 1, 1, _, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, 1, 1, 1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for x, row in enumerate(self.mini_map):
            for y, tile in enumerate(row):
                if tile:
                    self.world_map[(y, x)] = tile
        print('world_map:')
        print(self.world_map)
        print('values')

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100,
                      pos[1] * 100, 100, 100), 2) for pos in self.world_map]
