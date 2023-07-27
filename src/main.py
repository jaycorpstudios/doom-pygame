import pygame as pg
import sys
from config.settings import RES, FPS
from entities.map import Map
from entities.player import Player


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.new()

    def new(self):
        self.map = Map(self)
        self.player = Player(self)

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'FPS: {self.clock.get_fps():.1f}')
        self.player.update()

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    g = Game()
    g.run()
