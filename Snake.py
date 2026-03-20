import pygame as pg

class Snake:
    def __init__(self, width, height, square_size):
        self.square_size = square_size

        self.x = width // 2
        self.y = height // 2

        self.x_speed = 0
        self.y_speed = 0

        self.pixels = []
        self.length = 1

    def check_self_collision(self):
        head = [self.x, self.y]

        for pixel in self.pixels[:-1]:
            if pixel == head:
                return True

        return False

    def handle_input(self, key):
        if key == pg.K_DOWN:
            self.x_speed, self.y_speed = 0, self.square_size
        elif key == pg.K_UP:
            self.x_speed, self.y_speed = 0, -self.square_size
        elif key == pg.K_RIGHT:
            self.x_speed, self.y_speed = self.square_size, 0
        elif key == pg.K_LEFT:
            self.x_speed, self.y_speed = -self.square_size, 0

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

        self.pixels.append([self.x, self.y])

        if len(self.pixels) > self.length:
            del self.pixels[0]

    def draw(self, screen):
        for pixel in self.pixels:
            pg.draw.rect(screen, (255, 255, 255),
                         (pixel[0], pixel[1], self.square_size, self.square_size))