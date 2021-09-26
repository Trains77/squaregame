from time import sleep
import os
from shared import song, credits
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import pydub
from pygame.locals import *
pygame.mixer.init()
pygame.mixer.music.load(song)
pygame.mixer.music.play(-1)

# Please DO NOT add this audio content to the Youtube Content ID System. I have used background music which is owned by FesliyanStudios.
