import pygame


class Menu:

    def __init__ (self, screen):
        self.screen = screen
        self.menu_img = pygame.image.load("assets/images/menu_img.png")
        self.rect = self.menu_img.get_rect(left = 0, top = 0)

        self.options = ["JOGAR", "OPÇÕES", "SAIR"]
        self.selected = 0

    def draw_text(self, text, size, color, center):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size, bold=True)
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=center)
        self.screen.blit(surface, rect)

    def draw_glow_text(self, text, size, color, center):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size, bold=True)

        # glow
        glow_color = (0, 255, 100)
        for offset in range(1, 4):
            glow = font.render(text, True, glow_color)
            rect = glow.get_rect(center=center)
            rect.x += offset
            rect.y += offset
            self.screen.blit(glow, rect)

        # texto principal
        main = font.render(text, True, color)
        rect = main.get_rect(center=center)
        self.screen.blit(main, rect)

    def show_message(self, text):
        font = pygame.font.SysFont("Arial", 30, bold=True)

        start_time = pygame.time.get_ticks()
        duration = 1500  # 1.5 segundos

        while pygame.time.get_ticks() - start_time < duration:
            self.screen.blit(self.menu_img, self.rect)

            msg = font.render(text, True, (255, 255, 0))
            rect = msg.get_rect(center=(550, 500))
            self.screen.blit(msg, rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def run(self):
        pygame.mixer.music.load("assets/sounds/menu_music.ogg")
        pygame.mixer.music.play(-1)

        self.option_rects = []
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self.screen.blit(self.menu_img, self.rect)

            hovering = False

            for rect in self.option_rects:
                if rect.collidepoint(mouse_pos):
                    hovering = True
                    break

            if hovering:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        choice = self.options[self.selected]

                        if choice == "OPÇÕES":
                            self.show_message("Em desenvolvimento...")
                        else:
                            pygame.mixer.music.stop()
                            return choice
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        choice = self.options[self.selected]

                        if choice == "OPÇÕES":
                            self.show_message("Em desenvolvimento...")
                        else:
                            pygame.mixer.music.stop()
                            return choice

            self.option_rects = []
            start_y = 300

            for i, option in enumerate(self.options):
                center = (550, start_y + i * 50)

                font = pygame.font.SysFont("Lucida Sans Typewriter", 40, bold=True)
                surface = font.render(option, True, (255, 255, 255))
                rect = surface.get_rect(center=center)

                # hover com mouse
                if rect.collidepoint(mouse_pos):
                    self.selected = i

                self.option_rects.append(rect)

                if i == self.selected:
                    self.draw_glow_text(option, 40, (255, 255, 255), center)
                else:
                    self.draw_text(option, 40, (200, 255, 200), center)
            pygame.display.flip()