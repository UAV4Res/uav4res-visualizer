import pygame
from typing import Callable, Optional
from Rectangle import Rectangle
from InputManager import InputManager
from TextManager import TextManager
from TextureManager import TextureManager


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        normal_color=(255, 255, 255),
        hovered_color=(183, 183, 183),
        font_color=(0, 0, 0),
        disable_color=(183, 183, 183),
    ):
        self.rectangle = Rectangle(x, y, width, height)
        self.callback: Optional[Callable[[], None]] = None
        self.is_disabled = False
        self.border = 0
        self.border_radius = 15
        self.font_color = font_color  # Black
        self.normal_color = normal_color  # White
        self.hovered_color = hovered_color  # Gray
        self.disabled_color = disable_color  # Gray
        self.title = ""
        self.font_size = 24
        self.texture_id = ""
        self.is_hovered = False
        self.is_clicked = False
        self.background_texture_id = None

    def setHoveredColor(self, color):
        self.hovered_color = color

    def setNormalColor(self, color):
        self.normal_color = color

    def setBackgroundImage(self, texture_id: str):
        self.background_texture_id = texture_id

    def draw(self):
        # Determine the button color
        if self.is_disabled:
            color = self.disabled_color
        elif self.is_hovered:
            color = self.hovered_color
        else:
            color = self.normal_color

        # Draw the button box
        from Game import Game

        Game().getWindow().draw_box_with_radius(
            color=color,
            rect=pygame.Rect(
                self.rectangle.x(),
                self.rectangle.y(),
                self.rectangle.w(),
                self.rectangle.h(),
            ),
            radius=self.border_radius,
            border=self.border,
        )

        if self.background_texture_id:
            TextureManager().draw_texture(
                name=self.background_texture_id,
                position=(self.rectangle.x(), self.rectangle.y()),
                scale=(self.rectangle.w(), self.rectangle.h()),
            )

        TextManager().print(
            text=self.title,
            position=(
                self.rectangle.x() + self.rectangle.w() // 2,
                self.rectangle.y() + self.rectangle.h() // 2,
            ),
            color=self.font_color,
            font_size=self.font_size,
        )

    def update(self):
        if self.is_disabled:
            return

        # Update hover state
        self.is_hovered = False
        self.is_clicked = False

        self.is_hovered = InputManager().is_mouse_inside_rectangle(self.rectangle)
        self.is_clicked = self.is_hovered and InputManager().is_mouse_down(1)
        if self.is_clicked:
            if self.callback:
                self.callback()

    def set_border(self, border: int):
        self.border = border

    def set_title(self, title):
        self.title = title

    def set_font_size(self, font_size: int):
        self.font_size = font_size

    def on_click(self, callback: Callable[[], None]):
        self.callback = callback

    def disable(self):
        self.is_disabled = True

    def enable(self):
        self.is_disabled = False

    def set_texture(self, texture_id):
        self.texture_id = texture_id

    def set_border_radius(self, border_radius):
        self.border_radius = border_radius
