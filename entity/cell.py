from util.color import Color
from util.vector import Vect2d

from view.display import Display

class Cell:
    """
    Petite boule inanimée permettant d'augmenter le score du joueur
    """

    def __init__(self, pos:Vect2d) -> None:
        """
        Constructeur

        INPUT :
            pos : Vect2d, position de la cellule

        OUTPUT :
            None
        """

        self.pos = pos
        self.color = Color.randomColor()
        # On prend une couleur aléatoire
        self.radius = 5

    def display(self) -> None:
        """
        Procédure d'affichage de la cellule

        INPUT :
            None

        OUTPUT :
            None
        """

        Display.drawCircle(pos=self.pos, color=self.color, radius=self.radius)
        # Dessine un cercle

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.pos)
