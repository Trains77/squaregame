# Script Modules
import platform
import sys
import getpass
import colored
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
pygame.init()
from time import sleep
from shared import credits, size, GameName, square2size, square_color
from colored import fore, back, style

# Credits
if credits == 1:
    print(fore.GREEN)
    print("Program by Me")
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
import music

# Display
screen = pygame.display.set_mode(size)
pygame.display.set_caption(GameName)
done = False
clock = pygame.time.Clock()
# Square 2
square2x1 = 100
square2y1 = 100
# Game
while not done:
    # clock.tick() limits the while loop to a max of 10 times per second.
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    square2x1 = square2x1 - 10
                if event.key == pygame.K_RIGHT:
                    square2x1 = square2x1 + 10
                if event.key == pygame.K_UP:
                    square2y1 = square2y1 - 10
                if event.key == pygame.K_DOWN:
                    square2y1 = square2y1 + 10
            if event.type == pygame.QUIT:  # If user clicked on close symbol
                done = True  # done variable that we are complete, so we exit this
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, square_color, [square2x1,square2y1,square2size,square2size])
        pygame.display.flip()
# Quite the execution when clicking on close
pygame.quit()
exit()
