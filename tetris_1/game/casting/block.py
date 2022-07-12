import random


class Block(object):
    """A solid, colored object that represents a set of bricks in the shape of a letter, falling from the top of the game scene.    
    Parent class for all blocks
    """
    
    rows = 20  # y
    columns = 10  # x

 
    def __init__(self, column, row, shape):
        S = [['.....',
            '......',
            '..00..',
            '.00...',
            '.....'],
            ['.....',
            '..0..',
            '..00.',
            '...0.',
            '.....']]

        Z = [['.....',
            '.....',
            '.00..',
            '..00.',
            '.....'],
            ['.....',
            '..0..',
            '.00..',
            '.0...',
            '.....']]

        I = [['..0..',
            '..0..',
            '..0..',
            '..0..',
            '.....'],
            ['.....',
            '0000.',
            '.....',
            '.....',
            '.....']]

        O = [['.....',
            '.....',
            '.00..',
            '.00..',
            '.....']]

        J = [['.....',
            '.0...',
            '.000.',
            '.....',
            '.....'],
            ['.....',
            '..00.',
            '..0..',
            '..0..',
            '.....'],
            ['.....',
            '.....',
            '.000.',
            '...0.',
            '.....'],
            ['.....',
            '..0..',
            '..0..',
            '.00..',
            '.....']]

        L = [['.....',
            '...0.',
            '.000.',
            '.....',
            '.....'],
            ['.....',
            '..0..',
            '..0..',
            '..00.',
            '.....'],
            ['.....',
            '.....',
            '.000.',
            '.0...',
            '.....'],
            ['.....',
            '.00..',
            '..0..',
            '..0..',
            '.....']]

        T = [['.....',
            '..0..',
            '.000.',
            '.....',
            '.....'],
            ['.....',
            '..0..',
            '..00.',
            '..0..',
            '.....'],
            ['.....',
            '.....',
            '.000.',
            '..0..',
            '.....'],
            ['.....',
            '..0..',
            '.00..',
            '..0..',
            '.....']]

        shapes = [S, Z, I, O, J, L, T]
        shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
        # index 0 - 6 represent shape
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3

    def shape_to_block(shape):
        """Converts shapes to blocks
        
        Arg: shape
        
        """
        positions = []
        format = shape.shape[shape.rotation % len(shape.shape)]
    
        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((shape.x + j, shape.y + i))
    
        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)
    
        return positions

    
