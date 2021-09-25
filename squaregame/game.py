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
from shared import credits, size, GameName, square_size, square_color, evil_square_color, good_square_color, game_border1, game_border2
from colored import fore, back, style
import math
import random

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
# Square 1
square1x1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
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
        if square2x1 == square3x1:
            if square2y1 == square3y1:
                print(fore.LIGHT_GREEN_2 + "You Win!" + style.RESET)
                done = True
        if square2x1 == square1x1:
            if square2y1 == square1y1:
                print(fore.RED + "You Died!" + style.RESET)
                done = True
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
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, square_color, [square2x1,square2y1,square_size,square_size])
        pygame.draw.rect(screen, evil_square_color, [square1x1,square1y1,square_size,square_size])
        pygame.draw.rect(screen, good_square_color, [square3x1,square3y1,square_size,square_size])
        pygame.display.flip()
# Quite the execution when clicking on close
pygame.quit()
exit()
