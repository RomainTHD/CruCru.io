if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.color import Color
from util.vector import Vect2d

from view.display import Display

from view.camera import Camera

class Cell:
    """Petite boule inanimée permettant d'augmenter le score du joueur

    Attributs:
        color (tuple of 4 int): couleur de la cellule en RGBA
        pos (Vect2d): position de la cellule
        radius (int): rayon de la cellule
        score (int): score que cette cellule donnera une fois mangée
    """

    BASE_RADIUS = 5

    def __init__(self, pos: Vect2d) -> None:
        """
        Constructeur

        Args:
            pos (Vect2d): position de la cellule
        """

        self.color = Color.randomColor()
        # On prend une couleur aléatoire

        self.pos = pos

        self.radius = self.BASE_RADIUS
        self.score = 1

    def display(self) -> None:
        """Procédure d'affichage de la cellule"""

        Display.drawCircle(pos=self.pos,
                           color=self.color,
                           radius=self.radius,
                           base_pos=Camera.pos)
