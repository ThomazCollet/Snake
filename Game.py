import pygame as pg
from Snake import Snake
from Food import Food
from Menu import *

class Game:
    def __init__(self, screen):

        self.width = 800
        self.height = 600

        self.screen = screen
        pg.display.set_caption("Snake Game")

        self.square_size = 10
        self.game_speed = 15
        self.clock = pg.time.Clock()

        self.snake = Snake(self.width, self.height, self.square_size)
        self.food = Food(self.width, self.height, self.square_size)

        self.score = 0

    def draw_score(self):
        font = pg.font.SysFont('Arial', 20)
        txt = font.render(f"Pontos: {self.score}", True, (255, 255, 255))
        self.screen.blit(txt, (10, 10))

    def run(self):
        game_over = False

        while not game_over:

            self.screen.fill((0, 0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_over = True
                elif event.type == pg.KEYDOWN:
                    self.snake.handle_input(event.key)

            # atualizar
            self.snake.move()

            # colisão com o próprio corpo
            if self.snake.check_self_collision():
                game_over = True

            # colisão com parede
            if (self.snake.x < 0 or self.snake.x >= self.width or
                self.snake.y < 0 or self.snake.y >= self.height):
                game_over = True

            # comer comida
            if self.snake.x == self.food.x and self.snake.y == self.food.y:
                self.snake.length += 1
                self.food.respawn()
                self.score += 50

            # desenhar
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.draw_score()

            pg.display.update()
            self.clock.tick(self.game_speed)