import pygame
import constants
from game.services.video_service import VideoService


class KeyboardService:
    """A keyboard service inteface."""

    def is_paused():            
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