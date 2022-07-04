from re import S
import pygame
import random
import sys
 
# initialising pygame
pygame.init()
pygame.font.init()

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T (with indexes between 0 and 6)
"""



# CONSTANTS
#==========================================================================================================================================
# Display
screen_width = 1200
screen_height = 900

# Max size of a set of bricks
block_size = 30

# Game scene
play_width = 380 
play_height = 720


# Game scene location
top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_width

#==========================================================================================================================================
# END CONSTANTS

# BLOCKS
#==========================================================================================================================================
# Build falling object in letter shapes

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

#==========================================================================================================================================
# END BRICKS

# PIECE CLASS
#==========================================================================================================================================
class Piece(object):
    # Change the name into Actor or Shape

    # Comment
    """A shape that participates in the game."""


    rows = 20  # y
    columns = 10  # x
 
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)] # For now the color follows the corresponding shape's index; may need to change this later
        self.rotation = 0  # number from 0-3



#==========================================================================================================================================
# END PIECE


# MAIN CLASS
#==========================================================================================================================================
def create_grid(locked_positions={}):
    # Change the name to draw_grid
    # Change Arg to "pos"
    """Draws a the grid on the game scene at the given position. The grid helps locate each blocks in real time.

        Args:
            
        
        Returns: 
        """
    # Creates a list in every row of our grid; so, we will 20 rows with 10 cutters
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
    
    #Find the corresponding position to the locked position
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    
    return grid



def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    # This one will go to the director class
    """Randomly generates falling blocks; picks a shape from the shapes' list. 

    Args:

    Returns: 
    
    """
    global shapes, shape_colors
 
    return Piece(5, 0, random.choice(shapes))
    

def draw_text_middle(text, size, color, surface):  
    pass
   
def draw_grid(surface, row, col, grid):
    # This one will be part of the video_service class
    # Change to draw_board
    """Draws all of our objects to the screen. 

        Args: surface, row, col, grid 
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* block_size, top_left_y + i * block_size, block_size, block_size), 0)
 
    # Draw the border frame for the game scene
    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5) # Change color to blue
    
def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface, grid):
    # Send all three (background, font and caption) to constants file and then import here
    surface.fill((0,0,0)) # Repale (0,0,0) by background = (0,250,154) -- mediumspringgreen	
    
    pygame.font.init()
    font = pygame.font.SysFont('tetris/assets/tetris-blocks-font/TetrisBlocks-P99g.ttf', 40)
    caption = font.render('TETRIS GAME', 1, (255,255,255)) # Tetris Title
    ######

    surface.blit(caption, (top_left_x + play_width / 2 - (caption.get_width() / 2), 30)) # prints the label on the screen 

    draw_grid(surface, grid)
    pygame.display.update()  
    

def main():
    # Change to director class
    """A person who directs the game."""
    
    # Import keyboard_service class here
    # KeyboardService()
    
    # KEYBOARD SERVICE
    # =======================================================================================================================================
    global grid
 
    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)
 
    change_piece = False
    is_playing = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock() # will be moved to the constants file, and then imported here
    fall_time = 0 # change to velocity
 
    while is_playing:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
                pygame.display.quit()
                pygame.quit()
                sys.exit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
 
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_SPACE:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
 
                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

        draw_window(win, grid)

    # =======================================================================================================================================
    # END KEYBOARD SERVICE

def main_menu(win):
    main(win)


win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")
main_menu(win)  # start game
#==========================================================================================================================================
# END MAIN
