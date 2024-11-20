import pygame
import cv2
import numpy as np
from GameState import GameState
from GameStateManager import GameStateManager
from InputManager import InputManager
from TextManager import TextManager
from Button import Button
from TextureManager import TextureManager


class MapBuildingState(GameState):
    def __init__(self):
        self.image = cv2.imread(
            "map1.jpeg"
        )  # Load the default image (replace with your map)
        self.result_image = None  # Will hold the processed map
        self.buttons = []

        # Load a texture for button background

        # Button: Go back to the previous state
        back_button = Button(x=100, y=500, width=150, height=60)
        back_button.set_title("Back")
        back_button.on_click(lambda: GameStateManager().pop_state())
        back_button.set_border(2)
        self.buttons.append(back_button)

        # Button: Navigate to Path Planning State
        path_planning_button = Button(x=500, y=500, width=150, height=60)
        path_planning_button.set_title("Path Planning")
        path_planning_button.disable()
        path_planning_button.set_border(2)
        from PathPlanningState import PathPlanningState

        # Button: Process map (Next step)
        next_button = Button(x=300, y=500, width=150, height=60)
        next_button.set_title("Build Map")
        next_button.on_click(
            lambda: (self.process_map(), path_planning_button.enable())
        )
        next_button.set_border(2)
        self.buttons.append(next_button)

        path_planning_button.on_click(
            lambda: GameStateManager().push_state(PathPlanningState())
        )
        self.buttons.append(path_planning_button)

    def process_map(self):
        if self.image is not None:
            self.result_image = self.getGroundMap()

    def getGroundMap(self):
        blurred_image = cv2.GaussianBlur(self.image, (5, 5), 0)
        gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, threshold1=0, threshold2=20)
        contours, _ = cv2.findContours(
            edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        contour_map = np.zeros_like(gray_image)
        cv2.drawContours(contour_map, contours, -1, (255), 1)  # Contour thickness = 1
        kernel = np.ones((5, 5), np.uint8)
        morph_image = cv2.morphologyEx(contour_map, cv2.MORPH_CLOSE, kernel)
        groundMapModel = cv2.bitwise_not(morph_image)
        return groundMapModel

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
            text="UAV4Res: Map Building",
            position=(Game().getWindow().width / 2, 100),
            color="black",
            font_size=50,
        )

        # Render buttons
        for button in self.buttons:
            button.draw()

        # Render original image
        if self.image is not None:
            original_surface = pygame.surfarray.make_surface(
                cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            )
            Game().getWindow().draw_image(
                texture=original_surface, position=(120, 200), scale=(200, 200)
            )  # Adjust position as needed

        # Render processed map if available
        if self.result_image is not None:
            result_surface = pygame.surfarray.make_surface(
                cv2.cvtColor(self.result_image, cv2.COLOR_GRAY2RGB)
            )
            Game().getWindow().draw_image(
                texture=result_surface, position=(420, 200), scale=(200, 200)
            )  # Adjust position as needed

    def clean(self):
        pass
