import pathlib
import pygame
from casting.color import Color


# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Tetris"
FRAME_RATE = 60

# display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")
CLOCK = pygame.time.Clock()

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 800
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

FIELD_WIDTH = 300  # meaning 300 // 10 = 30 width per block
FIELD_HEIGHT = 600  # meaning 600 // 20 = 20 height per block

BLOCK_SIZE = 30

TOP_LEFT_X = (SCREEN_WIDTH - FIELD_WIDTH) // 2
TOP_LEFT_Y = SCREEN_HEIGHT - FIELD_HEIGHT

# FONT
FONT_FILE = "tetris/assets/tetris-cufonfonts/Tetris.ttf"
FONT_SMALL = 32
FONT_MEDIUM = 40
FONT_LARGE = 60

# SOUND
BOUNCE_SOUND = "batter-complete/batter/assets/sounds/boing.wav"
WELCOME_SOUND = "batter-complete/batter/assets/sounds/start.wav"
OVER_SOUND = "batter-complete/batter/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
YELLOW = Color(255, 255, 0)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# fieldS
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "batter-complete/batter/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "batter-complete/batter/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"batter-complete/batter/assets/images/{n:03}.png" for n in range(100, 103)]
RACKET_WIDTH = 106
RACKET_HEIGHT = 28
RACKET_RATE = 6
RACKET_VELOCITY = 7

# BLOCK
BLOCK_GROUP = "BLOCKS"
BLOCK_IMAGES = {
    "b": [f"batter-complete/batter/assets/images/{i:03}.png" for i in range(10,19)],
    "g": [f"batter-complete/batter/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"batter-complete/batter/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"batter-complete/batter/assets/images/{i:03}.png" for i in range(40,49)]
}
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 28
BLOCK_DELAY = 0.5
BLOCK_RATE = 4
BLOCK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"