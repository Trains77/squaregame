# Script Modules
import platform
import sys
# import getpass
import colored
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
pygame.init()
from time import sleep
from shared import credits, size, GameName, square_size, square_color, evil_square_color, good_square_color, game_border1, game_border2, speed
from colored import fore, back, style
import math
import random
def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)
# Credits
if credits == 1:
    print(fore.BLUE)
    print("Program by Trains77")
    print()
    print("Song: '8 Bit Menu' by Fesliyan Studios")
    print()
    print("Made with Atom Editor")
    print()
    print("Utilizes Pygame 2.01")
    print()
    print("Other Used Resources: www.javatpoint.com")
    print(style.RESET)
# Audio
# moved
# Display
screen = pygame.display.set_mode(size)
pygame.display.set_caption(GameName)
done = False
clock = pygame.time.Clock()
bordered1 = 0
bordered2 = 0
bordered3 = 0
bordered4 = 0
bordered5 = 0
bordered6 = 0
bordered7 = 0
bordered8 = 0
bordered9 = 0
# Square 1
square1x1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1x2 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1x3 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1x4 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1x5 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1x6 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1x7 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1x8 = int(math.ceil(random.randint(10,450) / 10.0)) * 10


square1y1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y2 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y3 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y4 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y5 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y6 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y7 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y8 = int(math.ceil(random.randint(10,450) / 10.0)) * 10

# Square 2
square2x1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square2y1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
# Square 3
square3x1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square3y1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
# Game
while not done:
    # clock.tick() limits the while loop to a max of 10 times per second.
        clock.tick(10)
        if not square1x1 == game_border1:
            if bordered1 == 0:
                square1x1 = square1x1 + speed
        elif square1x1 == game_border1:
            bordered1 = 1
        if not square1x1 == game_border2:
            if bordered1 == 1:
                square1x1 = square1x1 - speed
        elif square1x1 == game_border2:
            bordered1 = 0
# end of stuff
        if not square1x2 == game_border1:
            if bordered2 == 0:
                square1x2 = square1x2 + speed
        elif square1x2 == game_border1:
            bordered2 = 1
        if not square1x2 == game_border2:
            if bordered2 == 1:
                square1x2 = square1x2 - speed
        elif square1x2 == game_border2:
            bordered2 = 0
# end of stuff
        if not square1x3 == game_border1:
            if bordered3 == 0:
                square1x3 = square1x3 + speed
        elif square1x3 == game_border1:
            bordered3 = 1
        if not square1x3 == game_border2:
            if bordered3 == 1:
                square1x3 = square1x3 - speed
        elif square1x3 == game_border2:
            bordered3 = 0
# end of stuff
        if not square1x4 == game_border1:
            if bordered4 == 0:
                square1x4 = square1x4 + speed
        elif square1x4 == game_border1:
            bordered4 = 1
        if not square1x4 == game_border2:
            if bordered4 == 1:
                square1x4 = square1x4 - speed
        elif square1x4 == game_border2:
            bordered4 = 0
# end of stuff
        if not square1x5 == game_border1:
            if bordered5 == 0:
                square1x5 = square1x5 + speed
        elif square1x5 == game_border1:
            bordered5 = 1
        if not square1x5 == game_border2:
            if bordered5 == 1:
                square1x5 = square1x5 - speed
        elif square1x5 == game_border2:
            bordered5 = 0
# end of stuff
        if not square1x6 == game_border1:
            if bordered6 == 0:
                square1x6 = square1x6 + speed
        elif square1x6 == game_border1:
            bordered6 = 1
        if not square1x6 == game_border2:
            if bordered6 == 1:
                square1x6 = square1x6 - speed
        elif square1x6 == game_border2:
            bordered6 = 0
# end of stuff
        if not square3y1 == game_border1:
            if bordered7 == 0:
                square3y1 = square3y1 + speed
        elif square3y1 == game_border1:
            bordered7 = 1
        if not square3y1 == game_border2:
            if bordered7 == 1:
                square3y1 = square3y1 - speed
        elif square3y1 == game_border2:
            bordered7 = 0
# end of stuff
        if not square1y8 == game_border1:
            if bordered9 == 0:
                square1y8 = square1y8 + speed
        elif square1y8 == game_border1:
            bordered9 = 1
        if not square1y8 == game_border2:
            if bordered9 == 1:
                square1y8 = square1y8 - speed
        elif square1y8 == game_border2:
            bordered9 = 0
# end of stuff
        if not square1y7 == game_border1:
            if bordered8 == 0:
                square1y7 = square1y7 + speed
        elif square1y7 == game_border1:
            bordered8 = 1
        if not square1y7 == game_border2:
            if bordered8 == 1:
                square1y7 = square1y7 - speed
        elif square1y7 == game_border2:
            bordered8 = 0
# end of stuff
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not square2x1 == game_border2:
                        square2x1 = square2x1 - 10
                if event.key == pygame.K_RIGHT:
                    if not square2x1 == game_border1:
                        square2x1 = square2x1 + 10
                if event.key == pygame.K_UP:
                    if not square2y1 == game_border2:
                        square2y1 = square2y1 - 10
                if event.key == pygame.K_DOWN:
                    if not square2y1 == game_border1:
                        square2y1 = square2y1 + 10
            if event.type == pygame.QUIT:
                done = True
        screen.fill((1, 50, 32))
        player_square = pygame.draw.rect(screen, square_color, [square2x1,square2y1,square_size,square_size])
        evil_square = pygame.draw.rect(screen, evil_square_color, [square1x1,square1y1,square_size,square_size])
        evil_square1 = pygame.draw.rect(screen, evil_square_color, [square1x2,square1y2,square_size,square_size])
        evil_square2 = pygame.draw.rect(screen, evil_square_color, [square1x3,square1y3,square_size,square_size])
        evil_square3 = pygame.draw.rect(screen, evil_square_color, [square1x4,square1y4,square_size,square_size])
        evil_square4 = pygame.draw.rect(screen, evil_square_color, [square1x5,square1y5,square_size,square_size])
        evil_square5 = pygame.draw.rect(screen, evil_square_color, [square1x6,square1y6,square_size,square_size])
        evil_square6 = pygame.draw.rect(screen, evil_square_color, [square1x8,square1y8,square_size,square_size])
        evil_square7 = pygame.draw.rect(screen, evil_square_color, [square1x7,square1y7,square_size,square_size])

        good_square = pygame.draw.rect(screen, good_square_color, [square3x1,square3y1,square_size,square_size])
#        image_display(screen, "Textures/dragons.png", [100,100])
        if pygame.Rect.colliderect(player_square, evil_square) == 1:
            print(fore.RED + "You Died!" + style.RESET)
            done = True
        if pygame.Rect.colliderect(player_square, evil_square1) == 1:
            print(fore.RED + "You Died!" + style.RESET)
            done = True
        if pygame.Rect.colliderect(player_square, evil_square2) == 1:
            print(fore.RED + "You Died!" + style.RESET)
            done = True
        if pygame.Rect.colliderect(player_square, evil_square3) == 1:
            print(fore.RED + "You Died!" + style.RESET)
            done = True
        if pygame.Rect.colliderect(player_square, evil_square4) == 1:
            print(fore.RED + "You Died!" + style.RESET)
            done = True
        if pygame.Rect.colliderect(player_square, evil_square5) == 1:
            print(fore.RED + "You Died!" + style.RESET)
            done = True
        if pygame.Rect.colliderect(player_square, good_square) == 1:
            print(fore.LIGHT_GREEN_2 + "You Win!" + style.RESET)
            done = True
        pygame.display.flip()
# Quite the execution when clicking on close
pygame.quit()
exit()
