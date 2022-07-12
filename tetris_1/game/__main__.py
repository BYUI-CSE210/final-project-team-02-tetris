import pygame
import constants
from directing.director import Director
from services.video_service import VideoService


def main(win):
    """Displays a main menu to direct the player to start, restart, or end the game
    
    Arg: win (represents the background)
    """
    play = Director()
    output = VideoService()

    is_playing = True
    
    while is_playing:
        win.fill((0,0,0))
        output.print_announcement(win, 'Press ENTER or SPACE key to start', constants.FONT_LARGE, (255,255,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
                    play.start_game()

    pygame.display.quit()

#main()  # start game

# setup the pygame window and give it a caption
win = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')


# call the main loop via the main
main(win)