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
                    (44, 468),
                    (108, 14),
                    (631, 459),
                    (62, 198),
                    (369, 185),
                ],
                fatals=[7, 5, 9, 5, 1],
                victim_needs=[2, 4, 5, 3, 1],
                rescue_position=[
                    (212, 456),
                    (151, 31),
                    (243, 252),
                    (99, 209),
                    (637, 263),
                ],
                rescue_resources=[5, 2, 3, 4, 1],
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
