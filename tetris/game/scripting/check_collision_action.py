import pygame
import constants
from pygame.locals import *
from pygame import mixer
from game.scripting.action import Action
from game.casting.block import Block


"""class CheckOverAction(Action):"""
class CheckCollisionAction:

    def __init__(self):
        pass
        
    
    def check_valid_spot(self, shape, grid):
        """Checks for a valid space that fits to the shape
        Args: shape, grid

        Returns: True or False (boolean)
        """
        valid_spots = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
        valid_spots = [j for sub in valid_spots for j in sub]
        formatted = Block.shape_to_block(shape)
    
        for pos in formatted:
            if pos not in valid_spots:
                if pos[1] > -1:
                    return False

        return True

    def clear_rows(self, grid, locked):
        """
        Checks and clears every filled row, and then shifted down all the blocks.

        Args: grid, locked

        Returns: inc (increment counter as integer)

        """
        inc = 0
        for i in range(len(grid)-1,-1,-1):
            row = grid[i]
            if (0, 0, 0) not in row:
                inc += 1
                # add positions to remove from locked
                ind = i
                for j in range(len(row)):
                    try:
                        del locked[(j, i)]
                        
                    except:
                        continue
                
        if inc > 0:
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newKey = (x, y + inc)
                    locked[newKey] = locked.pop(key)

                mixer.music.load(constants.CLEAR_ROW_SOUND)
                pygame.mixer.music.play()

        return inc


    def is_game_over(self, positions):
        """Checks if the player lost
        Arg: positions
        Returns: True or False (boolean)
        """
        for pos in positions:
            x, y = pos
            if y < 1:
                return True            

        return False
