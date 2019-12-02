"""Cellule"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")

import math

from util.color import Color
from util.vector import Vect2d

from view.display import Display

from view.camera import Camera

class Buisson:
    RADIUS = 50
    COLOR = Color.BUISSON_COLOR
    SPEED = 1/1000

    def __init__(self, pos: Vect2d) -> None:
        # On prend une couleur aléatoire

        self.pos = pos
        self.angle = 0
    
    def update(self):
        self.angle += Buisson.SPEED

    def display(self) -> None:
        for i in range(8):
            Display.drawTriangle(pos=self.pos,
                                 color=Buisson.COLOR,
                                 radius=Buisson.RADIUS*1.1,
                                 angle=i*math.pi/4 + self.angle,
                                 base_pos=Camera.pos)

        Display.drawCircle(pos=self.pos,
                           color=Buisson.COLOR,
                           radius=Buisson.RADIUS,
                           base_pos=Camera.pos)
