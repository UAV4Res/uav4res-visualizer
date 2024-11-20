import pygame
from Singleton import Singleton


@Singleton
class TextManager:
    def __init__(self):
        pygame.font.init()

    def print(
        self,
        text,
        position,
        font_path=None,
        font_size=24,
        color=(255, 255, 255),
        max_width=None,
    ):
        from Game import Game

        """
        Draw text on the screen, with optional line wrapping.

        Args:
            text (str): The text to display.
            position (tuple): (x, y) position to draw the text.
            font_path (str): Path to a custom font file (optional).
            font_size (int): Font size for the text.
            color (tuple): Text color as an (R, G, B) tuple.
            max_width (int): Maximum width for text wrapping (optional).
        """
        try:
            font = pygame.font.Font(font_path, font_size)
            # Split text into lines if max_width is provided
            lines = []
            if max_width:
                words = text.split(" ")
                current_line = []
                for word in words:
                    current_line.append(word)
                    rendered_line = font.render(" ".join(current_line), True, color)
                    if rendered_line.get_width() > max_width:
                        current_line.pop()
                        lines.append(" ".join(current_line))
                        current_line = [word]
                if current_line:
                    lines.append(" ".join(current_line))
            else:
                lines = [text]

            # Draw each line
            y_offset = 0
            for line in lines:
                rendered_line = font.render(line, True, color)
                text_width, text_height = rendered_line.get_size()
                x = position[0] - text_width // 2
                y = position[1] + y_offset - (text_height * len(lines)) // 2
                Game().getWindow().screen.blit(rendered_line, (x, y))
                y_offset += text_height
        except Exception as e:
            print(f"Error drawing font: {e}")
