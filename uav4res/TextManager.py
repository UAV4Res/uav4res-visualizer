import pygame
from Singleton import Singleton


@Singleton
class TextManager:
    def __init__(self):
        pygame.font.init()

    def print(
        self, text, position, font_path=None, font_size=24, color=(255, 255, 255)
    ):
        from Game import Game

        """
        Draw text on the screen.

        Args:
            text (str): The text to display.
            position (tuple): (x, y) position to draw the text.
            font_path (str): Path to a custom font file (optional).
            font_size (int): Font size for the text.
            color (tuple): Text color as an (R, G, B) tuple.
        """
        try:
            font = pygame.font.Font(font_path, font_size)
            rendered_text = font.render(text, True, color)
            # Get the width and height of the text
            text_width, text_height = rendered_text.get_size()

            # Calculate the position to center the text
            x = position[0] - text_width // 2
            y = position[1] - text_height // 2

            # Draw the text at the centered position
            Game().getWindow().screen.blit(rendered_text, (x, y))
        except Exception as e:
            print(f"Error drawing font: {e}")
