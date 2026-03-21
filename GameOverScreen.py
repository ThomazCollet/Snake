import pygame

class GameOverScreen:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score

        self.bg = pygame.image.load("assets/images/game_over_img.png")
        self.rect = self.bg.get_rect(topleft=(0, 0))

        self.options = ["JOGAR NOVAMENTE", "MENU PRINCIPAL"]
        self.selected = 0

        self.font = pygame.font.SysFont("Arial", 40, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 25)
        self.score_font = pygame.font.SysFont("Arial", 60, bold=True)

    def draw_text(self, text, font, color, center):
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=center)
        self.screen.blit(surface, rect)
        return rect

    def draw_glow_text(self, text, font, main_color, glow_color, center):
        # glow
        for offset in range(1, 5):
            glow = font.render(text, True, glow_color)
            rect = glow.get_rect(center=center)
            rect.x += offset
            rect.y += offset
            self.screen.blit(glow, rect)

        # texto principal
        main = font.render(text, True, main_color)
        rect = main.get_rect(center=center)
        self.screen.blit(main, rect)
        return rect

    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(self.bg, self.rect)

            score_value = str(self.score)
            pts_text = " PTS"

            # número
            self.draw_glow_text(
                score_value,
                self.score_font,
                (255, 255, 255),
                (0, 255, 150),
                (500, 220)
            )

            # PTS menor
            self.draw_text(
                pts_text,
                self.small_font,
                (200, 255, 200),
                (620, 230)
            )

            # 🎯 BOTÕES
            option_rects = []
            start_y = 380

            for i, option in enumerate(self.options):
                center = (550, start_y + i * 60)

                if i == self.selected:
                    rect = self.draw_glow_text(
                        option,
                        self.font,
                        (255, 255, 255),
                        (0, 255, 150),
                        center
                    )
                else:
                    rect = self.draw_text(
                        option,
                        self.font,
                        (180, 180, 180),
                        center
                    )

                if rect.collidepoint(mouse_pos):
                    self.selected = i

                option_rects.append(rect)

            # 🖱️ CURSOR (AGORA SIM FUNCIONA)
            hovering = any(rect.collidepoint(mouse_pos) for rect in option_rects)

            if hovering:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            # 🎮 EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return self.options[self.selected]

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        return self.options[self.selected]

            pygame.display.flip()