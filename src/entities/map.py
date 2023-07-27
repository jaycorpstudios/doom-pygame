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
    TILE_WIDTH = 100
    TILE_HEIGHT = 100

    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        # dictionary with (x, y) coordinates as keys and tiles as values
        self.world_map = {}
        self.get_map()
        for (posX, posY) in self.world_map:
            print(posX, posY)

    def get_map(self):
        for yIndex, row in enumerate(self.mini_map):
            for xIndex, tile in enumerate(row):
                if tile:
                    self.world_map[(xIndex, yIndex)] = tile

    def draw(self):
        [pg.draw.rect(self.game.screen,
                      'darkgray',
                      (posX * self.TILE_WIDTH,
                       posY * self.TILE_HEIGHT,
                       self.TILE_WIDTH,
                       self.TILE_HEIGHT),
                      2) for (posX,
                              posY) in self.world_map]
