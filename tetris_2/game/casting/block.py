
import random
import constants

class Block:
    """A solid, colored object that represents a set of bricks in the shape of a letter, falling from the top of the game scene."""

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = constants.SHAPES_COLORS[constants.SHAPES.index(shape)]
        self.rotation = 0  # number from 0-3


    def shape_to_block(shape):
        """Converts shapes to blocks
        
        Arg: shape

        Returns:
            Shapes positions
        
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


    def get_block():
        """Generates random shapes
        
        Returns:
            An instance of a block

        """
        global shapes, shape_colors
    
        return Block(5, 0, random.choice(constants.SHAPES))