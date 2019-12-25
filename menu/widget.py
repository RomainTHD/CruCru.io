from util.vector import Vect2d

class Widget:
    def __init__(self, pos: Vect2d, size: Vect2d, text: str) -> None:
        self.pos = pos
        self.size = size
        self.text = text

    def isMouseOver(self, mouse_pos: Vect2d) -> bool:
        """Fonction permettant de savoir si la souris est au dessus de ce slider ou non

        Args:
            mouse_pos (Vect2d): position de la souris

        Returns:
            res (bool): si la souris est sur le slider ou non
        """

        res = False

        if mouse_pos.x > self.pos.x and mouse_pos.x < self.pos.x + self.size.x:
            if mouse_pos.y > self.pos.y and mouse_pos.y < self.pos.y + self.size.y:
                res = True

        return res

    def on_click(self, mouse_pos) -> None:
        pass

    def when_display(widget, mouse_pos):
        return False

    def display(self, mouse_pos: Vect2d) -> bool:
        """Affichage du widget

        Args:
            mouse_pos (Vect2d): pour permettre un affichage différent
                                selon la position de la souris
        """

        return self.when_display(self, mouse_pos)
