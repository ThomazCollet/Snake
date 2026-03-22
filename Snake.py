import pygame as pg


class Snake:
    def __init__(self, width, height, square_size):
        self.square_size = square_size

        self.x = (width // self.square_size // 2) * self.square_size
        self.y = (height // self.square_size // 2) * self.square_size

        self.x_speed = 0
        self.y_speed = 0

        self.length = 5

        self.pixels = []

        for i in range(self.length):
            self.pixels.append([
                self.x - i * self.square_size,
                self.y
            ])

    def check_self_collision(self):
        # 🚫 não checa colisão se estiver parado
        if self.x_speed == 0 and self.y_speed == 0:
            return False

        head = self.pixels[-1]

        for pixel in self.pixels[:-1]:
            if pixel == head:
                return True

        return False
    def handle_input(self, key):
        if key == pg.K_RIGHT and self.x_speed == 0:
            self.x_speed, self.y_speed = self.square_size, 0

        elif key == pg.K_LEFT and self.x_speed == 0:
            self.x_speed, self.y_speed = -self.square_size, 0

        elif key == pg.K_UP and self.y_speed == 0:
            self.x_speed, self.y_speed = 0, -self.square_size

        elif key == pg.K_DOWN and self.y_speed == 0:
            self.x_speed, self.y_speed = 0, self.square_size

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

        self.pixels.append([self.x, self.y])

        if len(self.pixels) > self.length:
            del self.pixels[0]

    def draw(self, screen, offset_x=0, offset_y=0):
        for i, pixel in enumerate(self.pixels):
            if i == len(self.pixels) - 1:
                color = (0, 255, 150)
            else:
                color = (0, 200, 80)

            pg.draw.rect(
                screen,
                color,
                (pixel[0] + offset_x, pixel[1] + offset_y, self.square_size, self.square_size)
            )