import pygame
import random
import constants
from pygame.locals import *
from pygame import mixer
from casting.block import Block
from casting.grid import Block

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.init()
pygame.font.init()

mixer.init()
mixer.music.load(constants.PLAY_SOUND)
mixer.music.play()


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

        block = Block()

    # will go to collide_bricks_action and then change the function name to execute to apply polymorphism
    def check_valid_spot(self, shape, grid):
        """Checks for a valid space that fits to the shape
        Args: shape, grid

        Returns: True or False (boolean)
        """
        valid_spots = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
        valid_spots = [j for sub in valid_spots for j in sub]
        formatted = self.block.shape_to_block(shape)
    
        for pos in formatted:
            if pos not in valid_spots:
                if pos[1] > -1:
                    return False
    
        return True

    def start_game():
        """Starts the game"""
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

            # Call the draw_next_block function to display the newt shape on the screen
            draw_next_block(next_block, win)
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

                    


    
    
    

    

    
