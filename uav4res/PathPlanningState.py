import pygame
from GameState import GameState
from GameStateManager import GameStateManager
from InputManager import InputManager
from TextManager import TextManager
from Button import Button
from path_planning_visualizer import main
import json


class PathPlanningState(GameState):
    def __init__(self):
        self.buttons = []

        # Button: Go back to the previous state
        back_button = Button(x=300, y=550, width=150, height=60)
        back_button.set_title("Back")
        back_button.on_click(lambda: GameStateManager().pop_state())
        back_button.set_border(2)
        self.buttons.append(back_button)

        with open("./template.txt", "r") as file:
            s = file.read()
        templates = json.loads(s)

        for index, template in enumerate(templates):
            n_rescue_team, n_victim = template["type"]
            info = template["info"]

            column = index % 2
            row = index // 2
            width = 300
            height = 80
            pad = 20
            x = 80
            y = 200
            button = Button(
                x=x + column * (width + pad),
                y=y + row * (height + pad),
                width=width,
                height=80,
            )
            button.set_title(f"{n_rescue_team} Rescue Teams, {n_victim} Victims")
            button.set_font_size(30)
            button.set_border(2)

            def create_on_click(info):
                return lambda: main.run(
                    image_link="map1.jpeg",
                    victim_position=info["victim_positions"],
                    fatals=info["fatals"],
                    victim_needs=info["victim_needs"],
                    rescue_position=info["rescue_positions"],
                    rescue_resources=info["rescue_resources"],
                    assembly_area=[500, 20],
                )

            button.on_click(create_on_click(info))
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
            text="UAV4Res: Path Planning Visualizer",
            position=(Game().getWindow().width / 2, 100),
            color="black",
            font_size=50,
        )

        for button in self.buttons:
            button.draw()

    def clean(self):
        pass
