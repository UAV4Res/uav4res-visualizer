import pygame
from GameState import GameState
from GameStateManager import GameStateManager
from InputManager import InputManager
from TextManager import TextManager
from Button import Button
from path_planning_visualizer import main


class PathPlanningState(GameState):
    def __init__(self):
        self.buttons = []

        button = Button(x=280, y=300, width=200, height=100)
        button.set_title("Run Visualizer")
        button.set_font_size(30)
        button.set_border(2)
        button.on_click(
            lambda: main.run(
                image_link="map1.jpeg",
                victim_position=[
                    [205, 138],
                    [420, 369],
                    [389, 143],
                    [513, 126],
                    [244, 407],
                ],
                fatals=[2, 3, 4, 1, 5],
                victim_needs=[2, 2, 2, 1, 2],
                rescue_position=[
                    [382, 371],
                    [307,  21],
                    [372, 401],
                    [ 67,  69],
                    [412, 111]
                ],
                rescue_resources=[9, 4, 5, 3, 7],
                assembly_area=[400, 20],
            )
        )
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
            text="UAV4Res: Path Planning",
            position=(Game().getWindow().width / 2, 100),
            color="black",
            font_size=50,
        )

        for button in self.buttons:
            button.draw()

    def clean(self):
        pass
