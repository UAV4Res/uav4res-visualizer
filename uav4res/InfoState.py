import pygame
from GameState import GameState
from GameStateManager import GameStateManager
from InputManager import InputManager
from TextManager import TextManager
from Button import Button


class InfoState(GameState):
    def __init__(self):
        self.buttons = []

        from MenuState import MenuState

        button = Button(x=250, y=500, width=200, height=100)
        button.set_title("Back")
        button.on_click(lambda: GameStateManager().switch_state(MenuState()))
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
            text="Fluffy: UAV for Rescue",
            position=(Game().getWindow().width / 2, 100),
            color="black",
            font_size=50,
        )

        TextManager().print(
            text="Project from team Fluffy UET-VNU",
            position=(Game().getWindow().width / 2, 300),
            color="black",
            font_size=20,
        )

        for button in self.buttons:
            button.draw()

    def clean(self):
        pass
