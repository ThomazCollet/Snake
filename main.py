import pygame
from Game import Game
from Menu import Menu

def main():
    pygame.init()

    screen = pygame.display.set_mode((1100, 600))

    while True:
        menu = Menu(screen)
        choice = menu.run()

        if choice == "JOGAR":
            while True:
                game = Game(screen)
                result = game.run()

                if result == "RESTART":
                    continue  # reinicia o jogo

                elif result == "MENU":
                    break  # volta pro menu

        elif choice == "SAIR":
            pygame.quit()
            quit()
if __name__ == "__main__":
    main()
