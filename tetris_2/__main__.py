import pygame
import constants
from game.directing.director import Director
from game.services.video_service import VideoService

director = Director()


def main():
    
    director.start_game()

if __name__ == "__main__":
    main()




    