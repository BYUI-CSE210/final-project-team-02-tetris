import pygame
import constants
from game.directing.director import Director
from game.services.video_service import VideoService
from game.casting.background import Background
from game.casting.sound import Sound
from pygame.locals import *
from pygame import mixer



def main():
    director = Director()
    director.start_game()

# game actually starts with the main menu
def __launch__(win):
    """Displays a main menu to direct the player to start, restart, or end the game
    
    Arg: win (represents the background)
    """
    is_playing = True
    
    bg = Background(constants.BACKGROUND_IMAGE, [0,0])
    
    Sound.welcome_sound()
    
    # Enter the game loop
    while is_playing:        

        win.fill(constants.BLACK)        

        # Print background image and welcome message
        win.blit(bg.image, bg.rect)
        VideoService.draw_title(win, constants.PREP_TO_LAUNCH, constants.FONT_XLARGE, constants.YELLOW)
        VideoService.draw_text(win, constants.ENTER_TO_START, constants.FONT_MEDIUM, constants.PURPLE)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
                    mixer.music.stop() # stop welcome music
                    main()

    pygame.display.quit()


# setup the pygame window and give it a caption
win = constants.WINDOW
constants.CAPTION


# call the main loop via the launch
__launch__(win)



    