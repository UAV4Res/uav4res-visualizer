import pygame
from GameState import GameState
from GameStateManager import GameStateManager
from InputManager import InputManager
from TextManager import TextManager
from Button import Button


class PathPlanningState(GameState):
    def __init__(self):
        self.buttons = []
        button = Button(x=250, y=250, width=200, height=100)
        button.set_title("Path planning")
        from PlayState import PlayState

        button.on_click(lambda: GameStateManager().switch_state(PlayState()))
        self.buttons.append(button)

        button = Button(x=250, y=450, width=200, height=100)
        button.set_title("Back")
        button.on_click(lambda: GameStateManager().pop_state())
        self.buttons.append(button)

    def update(self):
        for button in self.buttons:
            button.update()

    def handle_events(self):
        from PlayState import PlayState

        if InputManager().is_key_down(pygame.K_RETURN):
            GameStateManager().switch_state(PlayState())

    def render(self):
        from Game import Game

        Game().window.fill("white")
        TextManager().print(
            text="Path Planning",
            position=(Game().getWindow().width / 2, 100),
            color="black",
            font_size=50,
        )
        for button in self.buttons:
            button.draw()

    def clean(self):
        pass
