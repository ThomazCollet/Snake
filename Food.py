import pygame as pg
import random

class Food:
    def __init__(self, width, height, square_size):
        self.width = width
        self.height = height
        self.square_size = square_size
        self.x, self.y = self.generate_position()

    def generate_position(self):
        x = round(random.randrange(0, (self.width - self.square_size)) / self.square_size) * self.square_size
        y = round(random.randrange(0, (self.height - self.square_size)) / self.square_size) * self.square_size
        return x, y

    def respawn(self):
        self.x, self.y = self.generate_position()

    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.square_size, self.square_size))