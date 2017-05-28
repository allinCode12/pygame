#My First Game Development!!

import pygame

pygame.init()

MyDisplay = pygame.display.set_mode((1000, 800))

pygame.display.set_caption("My First Game")

Game_Time = pygame.time.Clock()

CrashFail = False

while not CrashFail:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CrashFail = True

        print(event)

    pygame.display.update()
    #define frames per second
    Game_Time.tick(60)


pygame.quit()
quit()
