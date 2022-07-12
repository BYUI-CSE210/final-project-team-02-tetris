import pygame
import constants


class Grid:
    """creates the playspace 
    
    Args: grid, sx, sy
    """

    def __init__(self):

        grid = [[(0,0,0) for x in range(10)] for x in range(20)]
        sx = constants.TOP_LEFT_X
        sy = constants.TOP_LEFT_Y


    def create_grid(locked_spots={}, grid):
        """Creates a mutlidimensional list with 20 rows and 10 columns to keep track of the bricks in the falling blocks. 
    
        Arg: locked_spots

        Returns: grid (multidimensional list)
        """
        # loop through the locked positions and modify our blank grid to show these pieces.
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j,i) in locked_spots:
                    c = locked_spots[(j,i)]
                    grid[i][j] = c
        return grid


    def draw_grid(background, row, col, sx, sy):
        """Draws the grid lines on the game scene"""
        # This function draws the grey grid lines that we see

        for i in range(row):
            pygame.draw.line(background, (128,128,128), (sx, sy+ i*30), (sx + constants.FIELD_WIDTH, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(background, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + constants.FIELD_HEIGHT))  # vertical lines
    

    



