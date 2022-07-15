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
from game.casting.sound import Sound



class KeyboardService:
    """A keyboard service interface."""

    def __init__(self):
        self.collide = CheckCollisionAction()
        self.play = Sound()
        

    def is_playing(self):
        """Starts the game"""
        global grid

        # Scores variables
        self.score = 0
        self.last_score = Score.max_score(self)
    
        locked_spots = {}  # (x,y):(255,0,0)
        grid = Grid.create_grid(locked_spots)
    
        change_block = False
        on = True
        current_block = Block.get_block()
        next_block = Block.get_block()
        clock = pygame.time.Clock()
        fall_time = 0

        level_time = 0 # variable to increase the speed of falling blocks and make the game more difficult
    
        while on:

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
                if not (self.collide.check_valid_spot(current_block, grid)) and current_block.y > 0:
                    # Play sound for falling block
                    self.play.block_fall_sound()
                    current_block.y -= 1
                    change_block = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    on = False
                    pygame.display.quit()
                    quit()
    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_block.x -= 1
                        if not self.collide.check_valid_spot(current_block, grid):
                            current_block.x += 1
    
                    elif event.key == pygame.K_RIGHT:
                        current_block.x += 1
                        if not self.collide.check_valid_spot(current_block, grid):
                            current_block.x -= 1
                    elif event.key == pygame.K_UP:
                        # rotate shape
                        current_block.rotation = current_block.rotation + 1 % len(current_block.shape)
                        if not self.collide.check_valid_spot(current_block, grid):
                            current_block.rotation = current_block.rotation - 1 % len(current_block.shape)

                
                    elif event.key == pygame.K_DOWN:
                        # move shape down
                        current_block.y += 2
                        if not self.collide.check_valid_spot(current_block, grid):
                            current_block.y -= 2
                            
                    elif event.key == pygame.K_SPACE:
                        self._is_paused()


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
                self.score += self.collide.clear_rows(grid, locked_spots) * 10 # Get score by multiplying increment counter integer by 10
                
                # call four times to check for multiple clear rows
                self.collide.clear_rows(grid, locked_spots)

                

            VideoService.prepare_scene(constants.WINDOW, grid, self.score, self.last_score)

            # Call the VideoService.draw_next_block function to display the newt shape on the screen
            VideoService.draw_next_block(next_block, constants.WINDOW)
            pygame.display.update()

            # Check if the player lost
            if self.collide.is_game_over(locked_spots):
                
                self.play.game_over_sound()

                VideoService.draw_text(constants.WINDOW, "YOU LOST!", constants.FONT_LARGE, constants.WHITE)
                pygame.display.update()
                pygame.time.delay(4000)
                #self.play.welcome_sound()
                
                #Score.update_score(self.score)

                on = False


    def _is_paused(self):
            
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
            

    