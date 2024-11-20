from GameState import GameState
from GameStateManager import GameStateManager
from TextManager import TextManager
from TextureManager import TextureManager
from Button import Button


class MenuState(GameState):
    def __init__(self):
        self.buttons = []

        button = Button(x=270, y=250, width=200, height=75)
        button.set_title("Start Demo")
        button.set_border(2)
        button.set_font_size(30)
        button.on_click(lambda: GameStateManager().push_state(MapBuildingState()))
        self.buttons.append(button)

        button = Button(x=270, y=350, width=200, height=75)
        button.set_title("Info")
        button.set_border(2)
        button.set_font_size(30)
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

        Game().getWindow().fill("white")
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

        for button in self.buttons:
            button.draw()

    def clean(self):
        pass
