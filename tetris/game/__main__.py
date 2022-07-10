import pygame
import random
import constants

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - game_board
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS

width = constants.SCREEN_WIDTH
height = constants.SCREEN_HEIGHT
scene_width = 300  # meaning 300 // 10 = 30 width per block
scene_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (width - scene_width) // 2
top_left_y = height - scene_height


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

def create_grid(locked_positions={}):
    """
    The way that we will keep track of pieces in the game is using a grid data structure. We will create a multidimensional list that contains 20 lists of 10 elements (rows and columns). Each element in the lists will be a tuple representing the color of the piece in that current position. This will allow us to draw all of the colored squares quite easily as we can simply loop through the multidimensional list.

    Arg: locked_positions (dictionary of key value pairs where each key is a position of a piece that has already fallen and each value is its 
        color. 
    """
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
    
    # loop through the locked positions and modify our blank grid to show these pieces.
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

def convert_shape_format(shape):
    """Converts shapes into blocks
    
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

def valid_space(shape, grid):
    """Checks for a valid space that fits to the shape
    Args: shape, grid

    Returns: True or False (boolean)
    """
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)
 
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
 
    return True

def check_lost(positions):
    """Checks if the player lost
    Arg: positions
    Returns: True or False (boolean)
    """
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def get_shape():
    """Generates random shapes"""
    global shapes, shape_colors
 
    return Block(5, 0, random.choice(shapes))

def draw_text_middle(background, text, size, color):  
    """Prints the text in the middle of the screen
    
    Args: text, size, color, background

    """
    font = pygame.font.SysFont(constants.FONT_FILE, size, bold=True)
    label = font.render(text, 1, color)

    background.blit(label, (top_left_x + scene_width /2 - (label.get_width()/2), top_left_y + scene_height/2 - label.get_height()/2))

   
def draw_grid(background, row, col):
    """Draws the grid lines on the game scene"""
    # This function draws the grey grid lines that we see
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(background, (128,128,128), (sx, sy+ i*30), (sx + scene_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(background, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + scene_height))  # vertical lines

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
    label = font.render('Next Shape', 1, (255,255,255))

    sx = top_left_x + scene_width + 50
    sy = top_left_y + scene_height/2 - 100
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
    background.blit(label, (top_left_x + scene_width / 2 - (label.get_width() / 2), 30))

    # current score
    font = pygame.font.SysFont(constants.FONT_FILE, constants.FONT_SMALL)
    label = font.render('Score: ' + str(score), 1, (255,255,255))

    sx = top_left_x + scene_width + 50
    sy = top_left_y + scene_height/2 - 100

    background.blit(label, (sx + 20, sy + 160))
    
    # last score
    label = font.render('High Score: ' + last_score, 1, (255,255,255))

    sx = top_left_x - 200
    sy = top_left_y + 200

    background.blit(label, (sx + 20, sy + 160))

 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(background, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)
 
    # draw grid and border
    draw_grid(background, 20, 10)
    pygame.draw.rect(background, (255, 0, 0), (top_left_x, top_left_y, scene_width, scene_height), 5)
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


def main():
    """Main function"""
    global grid

    # Scores variables
    score = 0
    last_score = max_score()
 
    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)
 
    change_block = False
    is_playing = True
    current_block = get_shape()
    next_block = get_shape()
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
        
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
    
        # Block FALLING CODE
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_block.y += 1
            if not (valid_space(current_block, grid)) and current_block.y > 0:
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
                    if not valid_space(current_block, grid):
                        current_block.x += 1
 
                elif event.key == pygame.K_RIGHT:
                    current_block.x += 1
                    if not valid_space(current_block, grid):
                        current_block.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_block.rotation = current_block.rotation + 1 % len(current_block.shape)
                    if not valid_space(current_block, grid):
                        current_block.rotation = current_block.rotation - 1 % len(current_block.shape)
 
                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_block.y += 1
                    if not valid_space(current_block, grid):
                        current_block.y -= 1


        shape_pos = convert_shape_format(current_block)

        # add color of Block to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1: # If we are not above the screen
                grid[y][x] = current_block.color
        
        # IF Block HIT GROUND
        if change_block:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_block.color
            current_block = next_block
            next_block = get_shape()
            change_block = False            
            score += clear_rows(grid, locked_positions) * 10 # Get score

            # call four times to check for multiple clear rows
            clear_rows(grid, locked_positions)

        game_board(win, grid, score, last_score)

        # Call the draw_next_shape function to display the newt shape on the screen
        draw_next_shape(next_block, win)
        pygame.display.update()

        # Check if the player lost
        if check_lost(locked_positions):
            draw_text_middle(win, "YOU LOST!", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            is_playing = False
            update_score(score)



def main_menu(win):
    """Displays a main menu to direct the player to start, restart, or end the game
    
    Arg: win
    """
    is_playing = True
    while is_playing:
        win.fill((0,0,0))
        draw_text_middle(win, 'Press Enter to start', 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    main()

    pygame.display.quit()

#main_menu()  # start game

# setup the pygame window and give it a caption
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tetris')


# call the main loop via the main_menu
main_menu(win)