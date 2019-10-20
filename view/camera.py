"""Caméra centrée sur le joueur"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.vector import Vect2d

class Camera:
    """Caméra

    Attributs:
        pos (Vect2d): position de la caméra
        window_center (Vect2d): centre de la fenêtre
    """

    pos = Vect2d()
    # Décalage de la caméra

    window_center = Vect2d()
    # Taille du centre de la fenêtre

    @classmethod
    def setWindowSize(cls, width: int, height: int) -> None:
        """Actualise la taille de la fenêtre

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
