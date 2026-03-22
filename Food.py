import pygame as pg
import random

class Food:
    def __init__(self, width, height, square_size):
        self.width = width
        self.height = height
        self.square_size = square_size
        self.x, self.y = self.generate_position()
        scale = int(self.square_size * 1.6)

        self.apple_img = pg.image.load("assets/images/apple.png").convert_alpha()
        self.apple_img = pg.transform.smoothscale(self.apple_img, (scale, scale))

    def generate_position(self):
        padding = self.square_size * 2  # margem de segurança

        x = random.randrange(
            padding // self.square_size,
            (self.width - padding) // self.square_size
        ) * self.square_size

        y = random.randrange(
            padding // self.square_size,
            (self.height - padding) // self.square_size
        ) * self.square_size

        return x, y

    def respawn(self):
        self.x, self.y = self.generate_position()

    def draw(self, screen, offset_x=0, offset_y=0):
        screen.blit(self.apple_img, (self.x + offset_x, self.y + offset_y))