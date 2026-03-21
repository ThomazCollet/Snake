import pygame


class Menu:

    def __init__ (self, screen):
        self.screen = pygame.display.set_mode((1100, 600))
        self.menu_img = pygame.image.load("assets/images/menu_img.png")
        self.rect = self.menu_img.get_rect(left = 0, top = 0)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, antialias=True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self, ):
        pygame.mixer.music.load("assets/sounds/menu_music.ogg")
        pygame.mixer.music.play(-1)
        while True:
            self.screen.blit(source=self.menu_img, dest=self.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()