from GameState import GameState
from GameStateManager import GameStateManager
from TextManager import TextManager
from TextureManager import TextureManager
from Button import Button


class MenuState(GameState):
    def __init__(self):
        self.buttons = []
        from MapBuildingState import MapBuildingState

        button = Button(x=230, y=300, width=300, height=100)
        button.set_title("Start Demo")
        button.set_border(2)
        button.set_font_size(40)
        button.on_click(lambda: GameStateManager().push_state(MapBuildingState()))
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
            position=(50 + Game().getWindow().width / 2, 180),
            color="black",
            font_size=50,
        )

        TextureManager().draw_texture(
            name="uet_logo",
            position=(50, 130),
            scale=(120, 120),
        )

        for button in self.buttons:
            button.draw()

    def clean(self):
        pass
