import pygame
import constants
from pygame.locals import *
from pygame import mixer

pygame.init()
pygame.font.init()

mixer.init()

class Sound:
    """Creates an instance of sound to be played"""
    def __init__(self):
        pass


    def welcome_sound():
        mixer.music.load(constants.WELCOME_SOUND)
        mixer.music.play()

    def clear_row_sound(self):
        mixer.music.load(constants.CLEAR_ROW_SOUND)
        mixer.music.play()

    def game_over_sound(self):
        mixer.music.load(constants.GAME_OVER_SOUND)
        mixer.music.play()

    def block_fall_sound(self):
        mixer.music.load(constants.BLOCK_FALL_SOUND)
        mixer.music.play()