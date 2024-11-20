import pygame
from GameState import GameState
from GameStateManager import GameStateManager
from InputManager import InputManager
from TextManager import TextManager
from TextureManager import TextureManager
from Button import Button


class InfoState(GameState):
    def __init__(self):
        self.buttons = []

        from MenuState import MenuState

        button = Button(x=280, y=500, width=200, height=65)
        button.set_title("Back")
        button.set_border(2)
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
            text="Fluffy (UET-VNU): UAV4Res",
            position=(50 + Game().getWindow().width / 2, 80),
            color="black",
            font_size=50,
        )

        TextureManager().draw_texture(
            name="uet_logo",
            position=(40, 30),
            scale=(100, 100),
        )

        TextManager().print(
            text="Project from team Fluffy UET-VNU, Project from team Fluffy UET-VNU, Project from team Fluffy UET-VNU",
            position=(Game().getWindow().width / 2, 300),
            color="black",
            font_size=30,
            max_width=500,
        )

        for button in self.buttons:
            button.draw()

    def clean(self):
        pass
