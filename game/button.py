"""Gestion des boutons"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.vector import Vect2d
from util.color import Color

from game.map import Map

from view.display import Display

class Button:
    """Bouton

    Attributs:
        pos (Vect2d): position du bouton
        size (Vect2d): largeur et hauteur du bouton
        on_click (function): fonction à appeler lors du clic sur ce bouton
        when_display (function): fonction à appeler lors de l'affichage de ce bouton
        text (text): texte sur le bouton
    """

    pos: Vect2d
    size: Vect2d
    on_click: 'function'
    when_display: 'function'
    text: str

    def __init__(self,
                 pos: Vect2d,
                 size: Vect2d,
                 text: str,
                 on_click: 'function' = lambda: None,
                 when_display: 'function' = lambda e: None,
                 when_init: 'function' = lambda e: None) -> None:

        """Constructeur

        Args:
            pos (Vect2d): position du bouton
            size (Vect2d): largeur et hauteur du bouton
            text (text): texte sur le bouton
            on_click (function): fonction à appeler lors du clic sur ce bouton
            when_display (function): fonction à appeler lors de l'affichage de ce bouton
            when_init (function): fonction à appeler lors de l'initialisation du bouton
        """

        self.pos = pos
        self.size = size

        self.on_click = on_click

        self.when_display = when_display
        self.text = text

        when_init(self)

    def isMouseOver(self, mouse_pos: Vect2d) -> bool:
        """Fonction permettant de savoir si la souris est au dessus de ce bouton ou non

        Args:
            mouse_pos (Vect2d): position de la souris

        Returns:
            res (bool): si la souris est sur le bouton ou non
        """

        res = False

        if mouse_pos.x > self.pos.x and mouse_pos.x < self.pos.x + self.size.x:
            if mouse_pos.y > self.pos.y and mouse_pos.y < self.pos.y + self.size.y:
                res = True

        return res

    def display(self, mouse_pos: Vect2d) -> bool:
        """Affichage du bouton

        Args:
            mouse_pos (Vect2d): pour permettre un affichage différent selon la position de la souris
        """

        return self.when_display(self, mouse_pos)

def buttonStart_Init(button: Button) -> None:
    """Initialisation du bouton Start"""

    button.color_hue = 100
    button.color_sat = 100

def buttonStart_Display(button: Button, mouse_pos: Vect2d) -> None:
    """Affichage du bouton Start"""

    if button.isMouseOver(mouse_pos):
        hand_cursor = True
        button.color_sat -= 3
    else:
        hand_cursor = False
        button.color_sat = 100
        button.color_hue += 1

    button_color = Color.HSVToRGB(button.color_hue, button.color_sat, 100)

    min_size = max(button.size.x, button.size.y)

    font_size = min_size*50/400

    Display.drawRect(button.pos,
                     button.size,
                     color=button_color,
                     fill=True)

    Display.drawText(button.text,
                     button.pos + button.size/2,
                     color=Color.BLACK,
                     size=font_size)

    return hand_cursor

def buttonEnd_Init(button: Button, first_try: bool) -> None:
    if first_try:
        button.alpha = 0

def buttonEnd_Display(button: Button, mouse_pos: Vect2d) -> None:
    """Affichage du texte de fin"""

    min_size = max(button.size.x, button.size.y)

    font_size = min_size*50/400

    Display.drawRect(Vect2d(0, 0), Display.size, (0, 0, 0, button.alpha))

    if button.alpha < 127:
        button.alpha += 1
    elif button.alpha < 255 and Map.game_finished:
        button.alpha += 1

    Display.drawText(button.text,
                     button.pos + button.size/2,
                     color=Color.RED,
                     size=font_size)

def buttonEndChoice_Display(button: Button, mouse_pos: Vect2d) -> None:
    """Affichage du bouton rejouer"""

    min_size = max(button.size.x, button.size.y)

    font_size = min_size*50/400

    if button.isMouseOver(mouse_pos):
        hand_cursor = True
        c = Color.BLACK
        f = True
    else:
        hand_cursor = False
        c = Color.RED
        f = False

    Display.drawRect(button.pos,
                     button.size,
                     color=Color.RED,
                     fill=f)

    Display.drawText(button.text,
                     button.pos + button.size/2,
                     color=c,
                     size=font_size)

    return hand_cursor
