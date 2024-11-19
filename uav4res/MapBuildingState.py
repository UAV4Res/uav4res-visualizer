import pygame
from GameState import GameState
from GameStateManager import GameStateManager
from InputManager import InputManager
from TextManager import TextManager
from Button import Button
from TextureManager import TextureManager


class MapBuildingState(GameState):
    def __init__(self):
        TextureManager().load_texture("boat", "map1.jpeg")
        self.buttons = []

        button = Button(x=250, y=250, width=300, height=200)
        button.setBackgroundImage("boat")
        self.buttons.append(button)

        button = Button(x=250, y=500, width=100, height=100)
        button.set_title("Back")
        button.on_click(lambda: GameStateManager().pop_state())
        self.buttons.append(button)

        button = Button(x=500, y=500, width=100, height=100)
        button.set_title("Next step")
        self.buttons.append(button)

        button = Button(x=500, y=600, width=100, height=100)
        button.set_title("Path Planning")
        from PathPlanningState import PathPlanningState

        button.on_click(lambda: GameStateManager().push_state(PathPlanningState()))
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
            text="Map Building Step 1: Chose a map",
            position=(Game().getWindow().width / 2, 100),
            color="black",
            font_size=50,
        )

        for button in self.buttons:
            button.draw()

    def clean(self):
        pass
