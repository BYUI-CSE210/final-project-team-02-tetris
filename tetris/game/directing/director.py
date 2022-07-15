import pygame
import random
import constants
from pygame.locals import *
from pygame import mixer
from game.casting.block import Block
from game.services.video_service import VideoService
from game.casting.grid import Grid
from game.scripting.check_collision_action import CheckCollisionAction
from game.casting.score import Score
from game.casting.sound import Sound
from game.services.keyboard_service import KeyboardService

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.init()
pygame.font.init()

class Director:
    """A person who directs the game."""

    def __init__(self):
        """Constructs a new Director using the specified video service.
        
        
        """
        self.key = KeyboardService()
        
    def start_game(self):
        self.key.is_playing()
        

    def is_gameOver(positions):
        """Checks if the player lost
        Arg: positions
        Returns: True or False (boolean)
        """
        for pos in positions:
            x, y = pos
            if y < 1:
                return True
        return False
    
    


    
        

                
    