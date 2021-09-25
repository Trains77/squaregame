import pygame
from pygame.locals import *
pygame.init()
done = False
size = [500, 500]

screen = pygame.display.set_mode(size)
while not done:
    # clock.tick() limits the while loop to a max of 10 times per second.
#        clock.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked on close symbol
                done = True  # done variable that we are complete, so we exit this loop

    # Clear the default screen background and set the white screen background
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("left")
                if event.key == pygame.K_RIGHT:
                    print("right")
                if event.key == pygame.K_UP:
                    print("UP")
                if event.key == pygame.K_DOWN:
                    print("DOWN")
