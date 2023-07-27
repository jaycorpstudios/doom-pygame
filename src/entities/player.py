import pygame as pg
from config.settings import player_config, WIDTH
from lib.utils.trigonometry import polar_to_cartesian
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = player_config['position']
        self.angle = player_config['angle']
        self.rotation_speed = player_config['rotation_speed']

    def movement(self):

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = player_config['speed'] * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.x += dx
        self.y += dy

        delta_angle = self.rotation_speed * self.game.delta_time

        if keys[pg.K_LEFT]:
            self.angle -= delta_angle
        if keys[pg.K_RIGHT]:
            self.angle += delta_angle

        self.angle %= 2 * math.pi

    def update(self):
        self.movement()

    def draw(self):
        pg.draw.circle(self.game.screen, 'green',
                       (self.x * 100, self.y * 100), 15)
        start_position = (self.x * 100, self.y * 100)
        end_position = polar_to_cartesian(
            WIDTH, self.angle, (self.x * 100, self.y * 100))
        pg.draw.line(
            self.game.screen,
            'yellow',
            start_position,
            end_position,
            2)

    @property
    def position(self):
        return self.x, self.y

    @property
    def map_position(self):
        return int(self.x), int(self.y)
