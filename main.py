import pygame
from Game import Game
from Menu import Menu

def main():
    pygame.init()

    screen = pygame.display.set_mode((1100, 600))

    menu = Menu(screen)
    choice = menu.run()

    if choice == "JOGAR":
        game = Game(screen)
        game.run()

    elif choice == "SAIR":
        pygame.quit()
        quit()
if __name__ == "__main__":
    main()
