import pygame
from GameState import GameState
from GameStateManager import GameStateManager
from InputManager import InputManager


class PlayState(GameState):
    def update(self):
        pass

    def handle_events(self):
        from MenuState import MenuState

        if InputManager().is_key_down(pygame.K_ESCAPE):
            GameStateManager().switch_state(MenuState())

    def render(self):
        from Game import Game

        Game().window.fill((0, 255, 0))

    def clean(self):
        pass
