import pygame
import random
import constants
from pygame.locals import *
from pygame import mixer

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.init()
pygame.font.init()

mixer.init()
mixer.music.load("tetris/assets/bensound-summer_ogg_music.wav")
mixer.music.play()

# BLOCK CLASS
# ==========================================================================================================================================
# SHAPE FORMATS

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


class Block(object):
    # To be change in Actor
    """
    Parent class for all blocks
    """
    rows = 20  # y
    columns = 10  # x
 
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3


# ==========================================================================================================================================
# END BLOCK CLASS


def create_grid(locked_spots={}):
    """Creates a mutlidimensional list with 20 rows and 10 columns to keep track of the bricks in the falling blocks. 
    
    Arg: locked_spots

    Returns: grid (multidimensional list)
    """
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
    
    # loop through the locked positions and modify our blank grid to show these pieces.
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_spots:
                c = locked_spots[(j,i)]
                grid[i][j] = c
    return grid

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

def check_valid_spot(shape, grid):
    """Checks for a valid space that fits to the shape
    Args: shape, grid

    Returns: True or False (boolean)
    """
    valid_spots = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    valid_spots = [j for sub in valid_spots for j in sub]
    formatted = shape_to_block(shape)
 
    for pos in formatted:
        if pos not in valid_spots:
            if pos[1] > -1:
                return False
 
    return True

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

def get_block():
    """Generates random shapes"""
    global shapes, shape_colors
 
    return Block(5, 0, random.choice(shapes))

def print_announcement(background, text, size, color):  
    """Prints the announcement for the player in the middle of the screen
    
    Args: text, size, color, background

    """
    font = pygame.font.SysFont(constants.FONT_FILE, size, bold=True)
    label = font.render(text, 1, color)

    background.blit(label, (constants.TOP_LEFT_X + constants.FIELD_WIDTH /2 - (label.get_width()/2), constants.TOP_LEFT_Y + constants.FIELD_HEIGHT/2 - label.get_height()/2))

   
def draw_grid(background, row, col):
    """Draws the grid lines on the game scene"""
    # This function draws the grey grid lines that we see
    sx = constants.TOP_LEFT_X
    sy = constants.TOP_LEFT_Y
    for i in range(row):
        pygame.draw.line(background, (128,128,128), (sx, sy+ i*30), (sx + constants.FIELD_WIDTH, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(background, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + constants.FIELD_HEIGHT))  # vertical lines

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

def draw_next_shape(shape, background):
    """Prepares and draws the next falling shape on the right side of the screen
    Args: shape, background

    """
    font = pygame.font.SysFont(constants.FONT_FILE, constants.FONT_SMALL)
    label = font.render('Next Block', 1, (255,255,255))

    sx = constants.TOP_LEFT_X + constants.FIELD_WIDTH + 50
    sy = constants.TOP_LEFT_Y + constants.FIELD_HEIGHT/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(background, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)

    background.blit(label, (sx + 10, sy- 30))

def game_board(background, grid, score=0, last_score = 0):
    """Draws all actors on the screen"""
    
    # Set game scene's background
    background.fill((0,0,0))
    
    # Tetris Title
    font = pygame.font.SysFont(constants.FONT_FILE, constants.FONT_LARGE)
    label = font.render('TETRIS', 1, (255,255,255)) 
    background.blit(label, (constants.TOP_LEFT_X + constants.FIELD_WIDTH / 2 - (label.get_width() / 2), 30))

    # current score
    font = pygame.font.SysFont(constants.FONT_FILE, constants.FONT_SMALL)
    label = font.render('Score: ' + str(score), 1, (255,255,255))

    sx = constants.TOP_LEFT_X + constants.FIELD_WIDTH + 50
    sy = constants.TOP_LEFT_Y + constants.FIELD_HEIGHT/2 - 100

    background.blit(label, (sx + 20, sy + 160))
    
    # last score
    label = font.render('High Score: ' + last_score, 1, (255,255,255))

    sx = constants.TOP_LEFT_X - 200
    sy = constants.TOP_LEFT_Y + 200

    background.blit(label, (sx + 20, sy + 160))

 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(background, grid[i][j], (constants.TOP_LEFT_X + j* 30, constants.TOP_LEFT_Y + i * 30, 30, 30), 0)
 
    # draw grid and border
    draw_grid(background, 20, 10)
    pygame.draw.rect(background, (255, 0, 0), (constants.TOP_LEFT_X, constants.TOP_LEFT_Y, constants.FIELD_WIDTH, constants.FIELD_HEIGHT), 5)
    pygame.display.update()


def update_score(nscore):
    """Creates a file to save score
    Arg: nscore
    """
    score = max_score()

    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))

def max_score():
    """Saves maximum scores earned by the player
    
    Returns: score (integer)
    """
    with open('tetris/assets/scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score

# MAIN CLASS
# ============================================================================================================================================

def main():
    """Main function"""
    global grid

    # Scores variables
    score = 0
    last_score = max_score()
 
    locked_spots = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_spots)
 
    change_block = False
    is_playing = True
    current_block = get_block()
    next_block = get_block()
    clock = pygame.time.Clock()
    fall_time = 0

    level_time = 0 # variable to increase the speed of falling blocks and make the game more difficult
 
    while is_playing:

        # Increase the speed as time goes on
        level_time += clock.get_rawtime()
        if level_time/1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005


        fall_speed = 0.27
        
        grid = create_grid(locked_spots)
        fall_time += clock.get_rawtime()
        clock.tick()
    
        # Block FALLING CODE
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_block.y += 1
            if not (check_valid_spot(current_block, grid)) and current_block.y > 0:
                current_block.y -= 1
                change_block = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
                pygame.display.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_block.x -= 1
                    if not check_valid_spot(current_block, grid):
                        current_block.x += 1
 
                elif event.key == pygame.K_RIGHT:
                    current_block.x += 1
                    if not check_valid_spot(current_block, grid):
                        current_block.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_block.rotation = current_block.rotation + 1 % len(current_block.shape)
                    if not check_valid_spot(current_block, grid):
                        current_block.rotation = current_block.rotation - 1 % len(current_block.shape)

            
                elif event.key == pygame.K_DOWN:
                    # move shape down
                    current_block.y += 4
                    if not check_valid_spot(current_block, grid):
                        current_block.y -= 4

                elif event.key == pygame.K_SPACE:
                        _is_paused()


        shape_pos = shape_to_block(current_block)

        # add color of Block to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1: # If we are not above the screen
                grid[y][x] = current_block.color
        
        # IF Block HIT GROUND
        if change_block:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_spots[p] = current_block.color
            current_block = next_block
            next_block = get_block()
            change_block = False            
            score += clear_rows(grid, locked_spots) * 10 # Get score

            # call four times to check for multiple clear rows
            clear_rows(grid, locked_spots)

        game_board(win, grid, score, last_score)

        # Call the draw_next_shape function to display the newt shape on the screen
        draw_next_shape(next_block, win)
        pygame.display.update()

        # Check if the player lost
        if is_gameOver(locked_spots):
            print_announcement(win, "YOU LOST!", constants.FONT_LARGE, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1000)
            is_playing = False
            update_score(score)


def _is_paused():
        
        pause = True
        
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False
                        
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
         
            print_announcement(win, "PAUSED", constants.FONT_MEDIUM, (0,255,255))
            pygame.display.update()

            

def main_menu(win):
    """Displays a main menu to direct the player to start, restart, or end the game
    
    Arg: win (represents the background)
    """
    is_playing = True
    while is_playing:
        win.fill((0,0,0))
        print_announcement(win, 'Press ENTER or SPACE key to start', constants.FONT_LARGE, (255,255,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
                    main()

    pygame.display.quit()

#main_menu()  # start game

# setup the pygame window and give it a caption
win = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')


# call the main loop via the main_menu
main_menu(win)


# ============================================================================================================================================
# END MAIN CLASS