# importar e dar inicio

import pygame, random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('snake')

# função para movimentar dentro do grid
def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0] and (c1[1] == c2[1]))

# definir as direções
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# definir tamanho da tela e cobra
snake = [(200,200), (210, 200), (220, 200)]
skin = pygame.Surface((10, 10))
skin.fill((255, 255, 255))

#definir tamanho, cor e direção da maçã
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
applePosition = on_grid_random()
caminho = LEFT

# função para desacelerar a movimentação
clock = pygame.time.Clock()

# traço de repetição do jogo
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

# função para controlar a cobra
    if event.type == KEYDOWN:
        if event.key == K_UP:
            caminho = UP
        if event.key == K_DOWN:
            caminho = DOWN
        if event.key == K_RIGHT:
            caminho = RIGHT
        if event.key == K_LEFT:
            caminho = LEFT

# definir que a cobra cresça quando colidir com a maça
    if collision(snake[0], applePosition):
        applePosition = on_grid_random()
        snake.append((0, 0))

# movimentação do final da cobra
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

# movimentação da cabeça da cobra [0]
    if caminho == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if caminho == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if caminho == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if caminho == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, applePosition)
    for pos in snake:
        screen.blit(skin, pos)

    pygame.display.update()