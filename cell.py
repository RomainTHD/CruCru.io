from color import Color
from display import Display

class Cell:
    """
    Petite boule inanimée.
    """

    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.color = Color.randomColor()
        self.radius = 5

    def display(self) -> None:
        Display.drawCircle(self.x, self.y, self.color, self.radius)
