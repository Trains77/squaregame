# Script Modules
import platform
import sys
import colored
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
pygame.init()
from time import sleep
import time
from shared import size, GameName, square_size, playerspeed, fps, square_color, evil_square_color, good_square_color, game_border1, game_border2, speed
from colored import fore, back, style
import math
import random
def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)
# Credits
import credits
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
bordered10 = 0
borderedG1 = 0
# Square 1
square1x1 = int(math.ceil(random.randint(game_border2,game_border1) / 10.0)) * 10
square1x2 = int(math.ceil(random.randint(game_border2,game_border1) / 10.0)) * 10
square1x3 = int(math.ceil(random.randint(game_border2,game_border1) / 10.0)) * 10
square1x4 = int(math.ceil(random.randint(game_border2,game_border1) / 10.0)) * 10
square1x5 = int(math.ceil(random.randint(game_border2,game_border1) / 10.0)) * 10
square1x6 = int(math.ceil(random.randint(game_border2,game_border1) / 10.0)) * 10
square1x7 = int(math.ceil(random.randint(game_border2,game_border1) / 10.0)) * 10
square1x8 = int(math.ceil(random.randint(game_border2,game_border1) / 10.0)) * 10
square1x9 = int(math.ceil(random.randint(game_border2,game_border1) / 10.0)) * 10

square1y1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y2 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y3 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y4 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y5 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y6 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y7 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y8 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square1y9 = int(math.ceil(random.randint(10,450) / 10.0)) * 10

# Square 2
# square2x1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
# square2y1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square2x1 = 0
square2y1 = 0
# Square 3
square3x1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
square3y1 = int(math.ceil(random.randint(10,450) / 10.0)) * 10
# Game
def create_evil_square(square_movement, squarey, squarex, border):
    if square_movement == "x":
        if not squarey == game_border1:
            if border == 0:
                squarey = squarey + speed
        elif squarey == game_border1:
            border = 1
        if not squarey == game_border2:
            if border == 1:
                squarey = squarey - speed
        elif squarey == game_border2:
            border = 0
    elif square_movement == "y":
        if not squarex == game_border1:
            if border == 0:
                squarex = squarex + speed
        elif squarex == game_border1:
            border = 1
        if not squarex == game_border2:
            if border == 1:
                squarex = squarex - speed
        elif squarex == game_border2:
            border = 0
    return squarey, squarex, border
while not done:
        clock.tick(fps)

        square1y1, square1x1, bordered1 = create_evil_square("x", square1y1, square1x1, bordered1)
        square1y2, square1x2, bordered2 = create_evil_square("x", square1y2, square1x2, bordered2)
        square1y3, square1x3, bordered3 = create_evil_square("x", square1y3, square1x3, bordered3)
        square1y4, square1x4, bordered4 = create_evil_square("x", square1y4, square1x4, bordered4)
        square1y5, square1x5, bordered5 = create_evil_square("x", square1y5, square1x5, bordered5)
        square1y6, square1x6, bordered6 = create_evil_square("x", square1y6, square1x6, bordered6)
        square1y7, square1x7, bordered7 = create_evil_square("x", square1y7, square1x7, bordered7)

        square1y7, square1x7, bordered7 = create_evil_square("y", square1y7, square1x7, bordered7)
        square1y8, square1x8, bordered8 = create_evil_square("y", square1y8, square1x8, bordered8)
        square1y9, square1x9, bordered9 = create_evil_square("y", square1y9, square1x9, bordered9)
        square3y1, square3x1, borderedG1 = create_evil_square("y", square3y1, square3x1, borderedG1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        state = pygame.key.get_pressed()
        if state[pygame.K_a]:
            if not square2x1 <= game_border2:
                square2x1 = square2x1 - playerspeed
            elif square2x1 <= game_border2:
                facing = "Left"
        if state[pygame.K_d]:
            if not square2x1 >= game_border1:
                square2x1 = square2x1 + playerspeed
            elif square2x1 >= game_border1:
                facing = "Right"
        if state[pygame.K_w]:
            if not square2y1 <= game_border2:
                square2y1 = square2y1 - playerspeed
            elif square2y1 <= game_border2:
                facing = "Up"
        if state[pygame.K_s]:
            if not square2y1 >= game_border1:
                square2y1 = square2y1 + playerspeed
            elif square2y1 >= game_border1:
                facing = "Down"
        if state[pygame.K_LEFT]:
            if not square2x1 <= game_border2:
                square2x1 = square2x1 - playerspeed
            elif square2x1 <= game_border2:
                facing = "Left"
        if state[pygame.K_RIGHT]:
            if not square2x1 >= game_border1:
                square2x1 = square2x1 + playerspeed
            elif square2x1 >= game_border1:
                facing = "Right"
        if state[pygame.K_UP]:
            if not square2y1 <= game_border2:
                square2y1 = square2y1 - playerspeed
            elif square2y1 <= game_border2:
                facing = "Up"
        if state[pygame.K_DOWN]:
            if not square2y1 >= game_border1:
                square2y1 = square2y1 + playerspeed
            elif square2y1 >= game_border1:
                facing = "Down"
        if state[pygame.K_ESCAPE]:
            done = True
            print("Quit")

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
        evil_square8 = pygame.draw.rect(screen, evil_square_color, [square1x9,square1y9,square_size,square_size])

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
        if pygame.Rect.colliderect(player_square, evil_square6) == 1:
            print(fore.RED + "You Died!" + style.RESET)
            done = True
        if pygame.Rect.colliderect(player_square, evil_square7) == 1:
            print(fore.RED + "You Died!" + style.RESET)
            done = True
        if pygame.Rect.colliderect(player_square, evil_square8) == 1:
            print(fore.RED + "You Died!" + style.RESET)
            done = True
        if pygame.Rect.colliderect(player_square, good_square) == 1:
            print(fore.LIGHT_GREEN_2 + "You Win!" + style.RESET)
            done = True
        pygame.display.flip()
# Quite the execution when clicking on close
pygame.quit()
exit()
