"""Buisson"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")

import math

from util.color import Color
from util.vector import Vect2d

from view.display import Display

from view.camera import Camera

class Bush:
    """Buisson

    Attributs:
        RADIUS (int): rayon du buisson
        SPEED (float): vitesse de rotation lors de l'affichage
        SHARPNESS (float): facteur de la taille des pics par rapport au rayon
        NB_TRIANGLES (int): nombre de triangles pour dessiner
                            Chaque triangle produira 3 pics
    """

    RADIUS = 50
    SPEED = 1/1000
    SHARPNESS = 0.1
    BASE_HEALTH = 18

    def __init__(self, pos: Vect2d) -> None:
        """Constructeur

        Args:
            pos (Vect2d): position du centre du buisson
        """

        self.pos = pos
        self.angle = 0
        self.health = Bush.BASE_HEALTH

        self.is_alive = True

    def update(self) -> None:
        """Update le buisson"""

        self.angle += Bush.SPEED

    def hit(self) -> None:
        """En cas de collision"""

        self.health -= 1

        if self.health == 0:
            self.is_alive = False

    def display(self) -> None:
        """Affichage du buisson"""

        c = Color.linearGradient(Color.BUSH_COLOR_FULL,
                                 Color.BUSH_COLOR_DEAD,
                                 1-(self.health-1)/(Bush.BASE_HEALTH-1))

        for i in range(self.health):
            # Les pics du buisson
            angle = i/self.health*2*math.pi + self.angle

            offset = Vect2d(math.cos(angle), math.sin(angle))*Bush.RADIUS*(1+Bush.SHARPNESS/3)

            Display.drawTriangle(pos=self.pos + offset,
                                 color=c,
                                 radius=Bush.RADIUS*Bush.SHARPNESS,
                                 angle=2*math.pi/self.health*i + self.angle,
                                 base_pos=Camera.pos)

        # Le cercle du buisson
        Display.drawCircle(pos=self.pos,
                           color=c,
                           radius=Bush.RADIUS,
                           base_pos=Camera.pos)
