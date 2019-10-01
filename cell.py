from color import Color
from display import Display
from vector import Vect2d

class Cell:
    """
    Petite boule inanimée.
    """

    def __init__(self, pos:Vect2d) -> None:
        self.pos = pos
        self.color = Color.randomColor()
        self.radius = 5

    def display(self) -> None:
        Display.drawCircle(self.pos, self.color, self.radius)
