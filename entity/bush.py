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
        COLOR (Color): couleur du buisson
        SPEED (float): vitesse de rotation lors de l'affichage
        SHARPNESS (float): facteur de la taille des pics par rapport au rayon
        NB_TRIANGLES (int): nombre de triangles pour dessiner
                            Chaque triangle produira 3 pics
    """

    RADIUS = 50
    COLOR = Color.BUSH_COLOR
    SPEED = 1/500
    SHARPNESS = 1.125
    NB_TRIANGLES = 6

    def __init__(self, pos: Vect2d) -> None:
        """Constructeur

        Args:
            pos (Vect2d): position du centre du buisson
        """

        self.pos = pos
        self.angle = 0

    def update(self) -> None:
        """Update le buisson"""

        self.angle += Bush.SPEED

    def display(self) -> None:
        """Affichage du buisson"""

        for i in range(Bush.NB_TRIANGLES):
            # Les pics du buisson
            Display.drawTriangle(pos=self.pos,
                                 color=Bush.COLOR,
                                 radius=Bush.RADIUS*Bush.SHARPNESS,
                                 angle=i/Bush.NB_TRIANGLES*2*math.pi/3 + self.angle,
                                 base_pos=Camera.pos)

        # Le cercle du buisson
        Display.drawCircle(pos=self.pos,
                           color=Bush.COLOR,
                           radius=Bush.RADIUS,
                           base_pos=Camera.pos)
