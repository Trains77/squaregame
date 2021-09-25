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
    
