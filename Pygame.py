#Snake Game

import pygame

pygame.init()
game_Display = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Racing')
clock = pygame.time.Clock()

Exit = False

while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True




    pygame.display.update()


pygame.quit()
quit()


