import pygame
import pygame as pg
import random

print('Setup Start')
pg.init()
pg.display.set_caption('Snake Game') # Nomeando a Janela
width = 800
height = 600
screen = pg.display.set_mode(size = (width, height)) # Criando A tela

# parâmetros da cobra
square_size = 10
game_speed = 15
clock = pg.time.Clock()
print('Setup end')

def generate_food_position():
    # Gerando a posição da comida de modo a garantir que a comida sempre esteja alinhada com a cobra
    food_x = round(random.randrange(0, (width - square_size)) / 20.0) * 20.0
    food_y = round(random.randrange(0, (height - square_size)) / 20.0) * 20.0

    return food_x, food_y

def spawn_food(size, food_x, food_y):
    pg.draw.rect(screen, (255, 255, 255), (food_x, food_y, size, size))

def draw_snake(size, pixels):
    for pixel in pixels:
        pg.draw.rect(screen, (255, 255, 255), (pixel[0], pixel[1], size, size))


def draw_score(score):
    font = pg.font.SysFont('Arial', 20)
    txt = font.render(f"Pontos: {score}", True, (255, 255, 255))
    screen.blit(txt, [1, 1])

def get_movement_from_key(key):
    if key == pg.K_DOWN:
        x_speed, y_speed = 0, square_size
    elif key == pg.K_UP:
        x_speed, y_speed = 0, -square_size
    elif key == pg.K_RIGHT:
        x_speed, y_speed = square_size, 0
    elif key == pg.K_LEFT:
        x_speed, y_speed = -square_size, 0

    return x_speed, y_speed

def game_loop():
    print('Loop Start')
    game_over = False

    x, y = width / 2, height / 2 # Posição inicial setada para o centro da tela
    speed_x, speed_y = 0, 0 # cobrinha incia parada

    snake_size = 1
    pixels = []

    food_x, food_y = generate_food_position()

    while not game_over:
        screen.fill((0, 0, 0))

        # Check for all events
        for event in pg.event.get():
            if event.type == pg.QUIT: # Close window
                game_over = True
                quit()  # End pygame
            elif event.type == pg.KEYDOWN:
                speed_x, speed_y = get_movement_from_key(event.key)


        # Desenhando a comida
        spawn_food(square_size, food_x, food_y)

        #Atualizando a posição da cobra
        if x < 0 or x > width or y < 0 or y > height:
            game_over = True
        x += speed_x
        y += speed_y

        # Desenhando a cobra
        pixels.append([x, y])
        if len(pixels) > snake_size:
            del pixels[0] # deletar o pixel mais antigo para a cobra "andar"

        for pixel in pixels[:-1]:
            if pixel == [x,y]: # A cobra se chocou com ela própria
                game_over = True
        draw_snake(square_size, pixels)
        draw_score((snake_size - 1) * 50) # Cada comida gera 50 pontos

        #Atualização da tela
        pygame.display.update()
        clock.tick(game_speed)

        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = generate_food_position()

game_loop()

