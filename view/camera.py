"""Caméra centrée sur le joueur"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.vector import Vect2d

from view.display import Display

class Camera:
    """Caméra

    Attributs:
        pos (Vect2d): position de la caméra
        window_center (Vect2d): centre de la fenêtre
    """

    pos: Vect2d
    # Décalage de la caméra

    window_center: Vect2d
    # Taille du centre de la fenêtre

    @classmethod
    def init(cls):
        """Initialisation de la caméra"""

        Display.execWhenResized(cls.whenResized)

        cls.pos = Vect2d(0, 0)
        cls.window_center = None

    @classmethod
    def whenResized(cls, width: int, height: int) -> None:
        """Quand la fenêtre change de taille

        Args:
            width (int): nouvelle largeur de la fenêtre
            height (int): nouvelle hauteur de la fenêtre
        """

        cls.window_center = Vect2d(width, height)/2

    @classmethod
    def setPos(cls, pos: Vect2d) -> None:
        """Actualise la position de la caméra

        Args:
            width (int): nouvelle largeur de la fenêtre
            height (int): nouvelle hauteur de la fenêtre
        """

        cls.pos = pos - cls.window_center
