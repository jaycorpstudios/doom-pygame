import pygame as pg
import sys
from settings import RES, FPS
from map import Map


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new()

    def new(self):
        self.map = Map(self)

    def draw(self):
        self.screen.fill('black')
        self.map.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'FPS: {self.clock.get_fps():.1f}')

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    g = Game()
    g.run()
