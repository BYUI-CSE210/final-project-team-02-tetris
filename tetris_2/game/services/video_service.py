import pygame
import constants


class VideoService:
    """A video service inteface."""

    def draw_text(background, text, size, color):  
        """Prints the announcement for the player in the middle of the screen
        
        Args: text, size, color, background

        """
        font = pygame.font.SysFont(constants.FONT_FILE, size, bold=True)
        label = font.render(text, 1, color)

        background.blit(label, (constants.TOP_LEFT_X + constants.FIELD_WIDTH /2 - (label.get_width()/2), constants.TOP_LEFT_Y + constants.FIELD_HEIGHT/2 - label.get_height()/2))

    
    def draw_grid(background, row, col):
        """Draws the grid lines on the game scene"""
        # This function draws the grey grid lines that we see
        sx = constants.TOP_LEFT_X
        sy = constants.TOP_LEFT_Y
        for i in range(row):
            pygame.draw.line(background, (128,128,128), (sx, sy+ i*30), (sx + constants.FIELD_WIDTH, sy + i * 30))  # horizontal lines
            for j in range(col):
                pygame.draw.line(background, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + constants.FIELD_HEIGHT))  # vertical lines


    def draw_next_block(shape, background):
        """Prepares and draws the next falling shape on the right side of the screen
        Args: shape, background

        """
        font = pygame.font.SysFont(constants.FONT_FILE, constants.FONT_SMALL)
        label = font.render('Next Block', 1, (255,255,255))

        sx = constants.TOP_LEFT_X + constants.FIELD_WIDTH + 50
        sy = constants.TOP_LEFT_Y + constants.FIELD_HEIGHT/2 - 100
        format = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(background, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)

        background.blit(label, (sx + 10, sy- 30))

    
    
