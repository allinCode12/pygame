#My First Game Development!!

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

#defining COLORS

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
purple = (128, 0, 128)

boy_width = 150
boy_height = 220
gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ward OFF!!")
GameTime = pygame.time.Clock()


#importing image
Boy = pygame.image.load('Boy.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gamedisplay, color, [thingx, thingy, thingw, thingh])


def boy(x,y):
    gamedisplay.blit(Boy, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return  textSurface, textSurface.get_rect()


def message_display(text):
    LargeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, LargeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gamedisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():

    x = (display_width * 0.37)
    y = (display_height * 0.56)


    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 15
    thing_width = 100
    thing_height = 100

    GameExit = False

    while not GameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 GameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change
        gamedisplay.fill(red)

        things(thing_startx, thing_starty, thing_width, thing_height, purple)
        thing_starty += thing_speed

        boy(x,y)

        if x > display_width- boy_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = -1 - thing_height
            thing_startx = random.randrange(0, display_width)


        if y > thing_starty + thing_height:
            print("y crossing over")

        if x > thing_startx and x < thing_startx + thing_width or x + boy_width < thing_startx + thing_width:

            crash()
            game_loop()

        if y > display_height- boy_height or y < 0:
            crash()

        pygame.display.update()
        GameTime.tick(60)


game_loop()
pygame.quit()
quit()
