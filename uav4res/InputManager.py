import pygame
from Singleton import Singleton
from Rectangle import Rectangle


@Singleton
class InputManager:
    def __init__(self):
        self.keys_down = set()  # Keys currently pressed
        self.keys_up = set()  # Keys just released
        self.keys_held = set()  # Keys held down
        self.mouse_down = set()  # Mouse buttons currently pressed
        self.mouse_up = set()  # Mouse buttons just released
        self.mouse_held = set()  # Mouse buttons held down
        self.mouse_pos = (0, 0)  # Mouse position
        self.quit = False  # Quit flag

    def update(self):
        from Game import Game

        # Reset transient state
        self.keys_down.clear()
        self.keys_up.clear()
        self.mouse_down.clear()
        self.mouse_up.clear()

        for event in pygame.event.get():
            # Process events
            if event.type == pygame.QUIT:
                Game().quit()
            elif event.type == pygame.KEYDOWN:
                self.keys_down.add(event.key)
                self.keys_held.add(event.key)
            elif event.type == pygame.KEYUP:
                self.keys_up.add(event.key)
                self.keys_held.discard(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down.add(event.button)
                self.mouse_held.add(event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_up.add(event.button)
                self.mouse_held.discard(event.button)
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos

    def is_key_down(self, key):
        return key in self.keys_down

    def is_key_up(self, key):
        return key in self.keys_up

    def is_key_held(self, key):
        return key in self.keys_held

    def is_mouse_down(self, button):
        return button in self.mouse_down

    def is_mouse_up(self, button):
        return button in self.mouse_up

    def is_mouse_held(self, button):
        return button in self.mouse_held

    def is_mouse_inside_rectangle(self, rectangle: Rectangle):
        mouse_x, mouse_y = self.mouse_pos

        return (
            rectangle.leftmost() <= mouse_x <= rectangle.rightmost()
            and rectangle.top() <= mouse_y <= rectangle.bottom()
        )
