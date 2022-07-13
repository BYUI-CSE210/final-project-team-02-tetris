import pygame
import random
import constants
from pygame.locals import *
from pygame import mixer
from game.casting.block import Block
from game.services.video_service import VideoService
from game.casting.grid import Grid
from game.scripting.check_collision_action import CheckCollisionAction
from game.casting.score import Score

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.init()
pygame.font.init()

mixer.init()
"""mixer.music.load(constants.WELCOME_SOUND)
mixer.music.play()"""

class Director:
    """A person who directs the game."""

    def __init__(self):
        """Constructs a new Director using the specified video service.
        
        
        """
        pass
        

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


    
    def start_game(self):
        """Starts the game"""
        global grid

        # Scores variables
        score = 0
        last_score = Score.max_score()
    
        locked_spots = {}  # (x,y):(255,0,0)
        grid = Grid.create_grid(locked_spots)
    
        change_block = False
        is_playing = True
        current_block = Block.get_block()
        next_block = Block.get_block()
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
            
            grid = Grid.create_grid(locked_spots)
            fall_time += clock.get_rawtime()
            clock.tick()
        
            # Block FALLING CODE
            if fall_time/1000 >= fall_speed:
                fall_time = 0
                current_block.y += 1
                if not (CheckCollisionAction.check_valid_spot(current_block, grid)) and current_block.y > 0:
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
                        if not CheckCollisionAction.check_valid_spot(current_block, grid):
                            current_block.x += 1
    
                    elif event.key == pygame.K_RIGHT:
                        current_block.x += 1
                        if not CheckCollisionAction.check_valid_spot(current_block, grid):
                            current_block.x -= 1
                    elif event.key == pygame.K_UP:
                        # rotate shape
                        current_block.rotation = current_block.rotation + 1 % len(current_block.shape)
                        if not CheckCollisionAction.check_valid_spot(current_block, grid):
                            current_block.rotation = current_block.rotation - 1 % len(current_block.shape)

                
                    elif event.key == pygame.K_DOWN:
                        # move shape down
                        current_block.y += 2
                        if not CheckCollisionAction.check_valid_spot(current_block, grid):
                            current_block.y -= 2
                            
                    elif event.key == pygame.K_SPACE:
                        self.is_paused()


            shape_pos = Block.shape_to_block(current_block)

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
                next_block = Block.get_block()
                change_block = False            
                score += CheckCollisionAction.clear_rows(grid, locked_spots) * 10 # Get score
                
                mixer.music.load(constants.BLOCK_FALL_SOUND)
                pygame.mixer.music.play()

                # call four times to check for multiple clear rows
                CheckCollisionAction.clear_rows(grid, locked_spots)

            VideoService.prepare_scene(constants.WINDOW, grid, score, last_score)

            # Call the VideoService.draw_next_block function to display the newt shape on the screen
            VideoService.draw_next_block(next_block, constants.WINDOW)
            pygame.display.update()

            # Check if the player lost
            if CheckCollisionAction.is_game_over(locked_spots):
                VideoService.draw_text(constants.WINDOW, "YOU LOST!", constants.FONT_LARGE, (255,255,255))
                pygame.display.update()
                pygame.time.delay(1000)
                is_playing = False
                Score.update_score(score)

                mixer.music.load(constants.GAME_OVER_SOUND)
                pygame.mixer.music.play()


    def is_paused(self):
            
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
        
            VideoService.draw_text(constants.WINDOW, "PAUSED", constants.FONT_MEDIUM, (0,255,255))
            pygame.display.update()
            pygame.mixer.music.stop()

        pygame.mixer.music.play()

                
    