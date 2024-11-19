import pygame
from Singleton import Singleton
from GameStateManager import GameStateManager
from InputManager import InputManager
from Window import Window
from MenuState import MenuState
from TextureManager import TextureManager


@Singleton
class Game:
    def __init__(self):
        self.isRunning = True
        self.FPS = 60
        self.window = Window(768, 700, 60)
        GameStateManager().push_state(MenuState())

    def update(self):
        GameStateManager().update()

    def handle_event(self):
        self.window.handle_FPS()
        InputManager().update()

        GameStateManager().handle_events()

    def render(self):
        self.window.fill("white")
        GameStateManager().render()
        pygame.display.flip()

    def quit(self):
        self.isRunning = False

    def clean(self):
        GameStateManager().clean()
        pygame.quit()

    def getWindow(self):
        return self.window
