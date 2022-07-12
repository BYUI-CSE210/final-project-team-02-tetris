import pygame
from scripting.action import Action


class CollideBricksAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the trail collides
    with the food, or the trail collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
    
    def is_game_over(positions):
        """Checks if the player lost
        Arg: positions
        Returns: True or False (boolean)
        """
        for pos in positions:
            x, y = pos
            if y < 1:
                return True
        return False

    def clear_rows(grid, locked):
        """
        Checks and clears every filled row, and then shifted down all the blocks.

        Args: grid, locked

        Returns: inc (integer)

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
        
        return inc