from vector import Vect2d
from display import Display
from color import Color

class Creature:
    base_radius = 20

    def __init__(self, pos:Vect2d, name:str, color:Color=Color.PINK):
        self.pos = pos.copy()

        self.radius = self.base_radius

        self.score = 0

        self.name = name

        self.color = color

    def update(self, width, height):
        pass

    def display(self) -> None:
        Display.drawCircle(pos=self.pos, color=self.color, radius=self.radius)
        Display.drawText(text_str=str(self.score), pos=self.pos, color=Color.WHITE)
