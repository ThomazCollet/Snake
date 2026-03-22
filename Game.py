import pygame as pg
from Snake import Snake
from Food import Food
from GameOverScreen import GameOverScreen

class Game:
    def __init__(self, screen):

        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

        pg.display.set_caption("Snake Game")

        self.square_size = 10
        self.game_speed = 15
        self.clock = pg.time.Clock()

        # 📐 Área jogável
        self.play_x = 115  # esquerda (já está bom)
        self.play_y = 129  # desce um pouquinho

        self.play_width = 890 # aumenta pra direita
        self.play_height = 360  # ajusta depois se precisar
        # 🖼️ Imagens (CARREGAR + ESCALAR)
        # 🖼️ Imagem única (background + frame juntos)
        self.background = pg.image.load("assets/images/background_and_frame.png").convert()
        self.background = pg.transform.scale(self.background, (self.width, self.height))


        # 🐍 Objetos do jogo
        self.snake = Snake(self.play_width, self.play_height, self.square_size)
        self.food = Food(self.play_width, self.play_height, self.square_size)

        # 🔊 Sons
        self.eat_sound = pg.mixer.Sound("assets/sounds/eat_sound.ogg")
        self.game_over_sound = pg.mixer.Sound("assets/sounds/game_over_sound.ogg")

        self.score = 0

    def draw_score(self):
        font = pg.font.SysFont('Arial', 30, bold=True)

        text = f"PONTOS: {self.score}"

        # 🎨 cor por faixa de pontuação
        if self.score < 250:
            color = (255, 255, 255)  # branco
        elif self.score < 750:
            color = (255, 215, 0)  # amarelo (dourado)
        else:
            color = (0, 255, 120)  # verde

        txt = font.render(text, True, color)

        # posição
        x, y = 20, 20

        # 📦 caixa de fundo
        padding = 10
        box = pg.Surface((txt.get_width() + padding * 2, txt.get_height() + padding * 2))
        box.set_alpha(130)
        box.fill((0, 0, 0))

        self.screen.blit(box, (x - padding, y - padding))

        # 🌑 sombra
        shadow = font.render(text, True, (0, 0, 0))
        self.screen.blit(shadow, (x + 2, y + 2))

        # ✨ texto
        self.screen.blit(txt, (x, y))

    def run(self):
        game_over = False

        while not game_over:

            self.screen.blit(self.background, (0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                elif event.type == pg.KEYDOWN:
                    self.snake.handle_input(event.key)

            # atualizar
            self.snake.move()

            # colisão com o próprio corpo
            if self.snake.check_self_collision():
                self.game_over_sound.play()
                pg.time.delay(500)  # pequeno delay pra ouvir o som
                game_over = True

            # colisão com parede
            head_x, head_y = self.snake.pixels[-1]

            if (head_x < 0 or head_x >= self.play_width or
                    head_y < 0 or head_y >= self.play_height):
                self.game_over_sound.play()
                pg.time.delay(500)  # pequeno delay pra ouvir o som
                game_over = True

            # comer comida
            head_x, head_y = self.snake.pixels[-1]

            if head_x == self.food.x and head_y == self.food.y:
                self.snake.length += 1
                self.food.respawn()
                self.score += 50

                self.eat_sound.play()

            # desenhar

            # desenhar jogo
            self.snake.draw(self.screen, self.play_x, self.play_y)
            self.food.draw(self.screen, self.play_x, self.play_y)
            self.draw_score()


            pg.display.update()
            self.clock.tick(self.game_speed)

        game_over_screen = GameOverScreen(self.screen, self.score)
        choice = game_over_screen.run()

        if choice == "JOGAR NOVAMENTE":
            return "RESTART"
        elif choice == "MENU PRINCIPAL":
            return "MENU"



