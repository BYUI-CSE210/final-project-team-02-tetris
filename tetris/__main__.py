import pygame
import constants
from game.directing.director import Director
from game.services.video_service import VideoService



def main():
    director = Director()
    director.start_game()
"""
if __name__ == "__main__":
    main()"""

def main_menu(win):
    """Displays a main menu to direct the player to start, restart, or end the game
    
    Arg: win (represents the background)
    """
    is_playing = True
    while is_playing:
        win.fill((0,0,0))
        VideoService.draw_text(win, 'Press ENTER or SPACE key to start', constants.FONT_LARGE, (255,255,0))
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

    