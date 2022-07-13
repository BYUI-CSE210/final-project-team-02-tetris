import pygame
import constants
from game.directing.director import Director
from game.services.video_service import VideoService
from game.casting.background import Background
from pygame.locals import *
from pygame import mixer



def main():
    director = Director()
    director.start_game()


def __main_menu__(win):
    """Displays a main menu to direct the player to start, restart, or end the game
    
    Arg: win (represents the background)
    """
    is_playing = True
    
    bg = Background(constants.BACKGROUND, [0,0])
    
    mixer.init()
    mixer.music.load(constants.WELCOME_SOUND)
    mixer.music.play()
    
    while is_playing:
        

        win.fill((0,0,0))        

        # Print background image
        win.blit(bg.image, bg.rect)
        VideoService.draw_title(win, constants.PREP_TO_LAUNCH, constants.FONT_XLARGE, (255,255,0))
        VideoService.draw_text(win, constants.ENTER_TO_START, constants.FONT_MEDIUM, (255,255,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
                    mixer.music.stop()
                    main()

    pygame.display.quit()


# setup the pygame window and give it a caption
win = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption(constants.GAME_TITLE)


# call the main loop via the main_menu
__main_menu__(win)

if __name__ == "__main_menu__":
    __main_menu__(win)

    