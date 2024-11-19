import pygame
from GameState import GameState
from GameStateManager import GameStateManager
from InputManager import InputManager
from TextManager import TextManager
from Button import Button


class MenuState(GameState):
    def __init__(self):
        self.buttons = []

        button = Button(x=250, y=250, width=200, height=100)
        button.set_title("Get Start")
        button.on_click(lambda: GameStateManager().push_state(MapBuildingState()))
        self.buttons.append(button)

        button = Button(x=250, y=350, width=200, height=100)
        button.set_title("Info")
        from MapBuildingState import MapBuildingState
        from InfoState import InfoState

        button.on_click(lambda: GameStateManager().push_state(InfoState()))
        self.buttons.append(button)

    def update(self):
        for button in self.buttons:
            button.update()

    def handle_events(self):
        pass

    def render(self):
        from Game import Game

        Game().window.fill("white")
        TextManager().print(
            text="Fluffy (UET-VNU): UAV for Rescue",
            position=(Game().getWindow().width / 2, 30),
            color="black",
            font_size=50,
        )
        for button in self.buttons:
            button.draw()

    def clean(self):
        pass
