"""Gestion des boutons"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from menu.widget import Widget

from util.vector import Vect2d
from util.color import Color

from game.map import Map

from view.display import Display

class Button(Widget):
    """Bouton

    Attributs:
        pos (Vect2d): position du bouton
        size (Vect2d): largeur et hauteur du bouton
        on_click (function): fonction à appeler lors du clic sur ce bouton
        when_display (function): fonction à appeler lors de l'affichage de ce bouton
        text (text): texte sur le bouton
    """

    pos: Vect2d # Position du bouton
    size: Vect2d # Taille du bouton
    on_click: 'function' # Fonction exécutée lors d'un clic
    when_display: 'function' # Fonction exécutée pour un affichage
    text: str # Texte affiché

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
            on_click (function): fonction à appeler lors du clic sur ce bouton, par défaut aucune
            when_display (function): fonction à appeler lors de l'affichage de ce bouton, par défaut aucune
            when_init (function): fonction à appeler lors de l'initialisation du bouton, par défaut aucune
        """

        super().__init__(pos, size, text)

        self.on_click = on_click

        self.when_display = when_display

        when_init(self)

def buttonStart_Init(button: Button) -> None:
    """Initialisation du bouton Start

    Args:
        button (Button): bouton start

    Attributs:
        color_hue (int): couleur du bouton
        color_sat (int): saturation du bouton
    """

    button.color_hue = 0
    button.color_sat = 100

def buttonStart_Display(button: Button, mouse_pos: Vect2d) -> bool:
    """Affichage du bouton Start

    Args:
        button (Button): bouton start
        mouse_pos (Vect2d): position de la souris

    Returns:
        hand_cursor (bool): si la souris doit être affichée comme une main ou un curseur
    """

    if button.isMouseOver(mouse_pos):
        # Arc-en-ciel
        hand_cursor = True
        button.color_sat = (button.color_sat - 3 + 100)%100
    else:
        # Flash épileptique
        hand_cursor = False
        button.color_sat = 100
        button.color_hue = (button.color_hue + 1)%360

    button_color = Color.HSVToRGB(button.color_hue, button.color_sat, 100)

    min_size = max(button.size.x, button.size.y)
    # Taille minimale entre la largeur et la hauteur

    font_size = min_size*50/400

    Display.drawRect(button.pos,
                     button.size,
                     color=button_color,
                     fill=True)
    # Rectangle du bouton

    Display.drawText(button.text,
                     button.pos + button.size/2,
                     color=Color.BLACK,
                     size=font_size)
    # Texte du bouton

    return hand_cursor

def buttonWinOrEnd_Init(button: Button, first_try: bool, color: Color) -> None:
    """Initialisation du bouton de fin

    Args:
        button (Button): bouton de fin
        first_try (bool): si ce bouton vient d'être initialisé pour la première fois ou non
        color (Color): couleur du bouton

    Attributs:
        color (Color): couleur du bouton
        alpha (int): composante alpha de la couleur
    """

    button.color = color

    if first_try:
        button.alpha = 0

def buttonEnd_Display(button: Button, mouse_pos: Vect2d) -> None:
    """Affichage du texte de fin"""

    min_size = max(button.size.x, button.size.y)

    font_size = min_size*50/400
    # Taille de la police

    Display.drawRect(Vect2d(0, 0), Display.size, (0, 0, 0, button.alpha))
    # Fondu transparent

    if button.alpha < 127:
        # Si le jeu est en cours on a un fondu jusqu'à 50%
        button.alpha += 1
    elif button.alpha < 255 and Map.game_finished:
        # Sinon le fondu se fait jusqu'à 100%
        button.alpha += 1

    Display.drawText(button.text,
                     button.pos + button.size/2,
                     color=button.color,
                     size=font_size)

def buttonEndChoice_Display(button: Button, mouse_pos: Vect2d) -> bool:
    """Affichage du bouton rejouer"""

    min_size = max(button.size.x, button.size.y)

    font_size = min_size*50/400

    if button.isMouseOver(mouse_pos):
        hand_cursor = True
        c = Color.BLACK
        f = True
    else:
        hand_cursor = False
        c = button.color
        f = False

    Display.drawRect(button.pos,
                     button.size,
                     color=button.color,
                     fill=f)

    Display.drawText(button.text,
                     button.pos + button.size/2,
                     color=c,
                     size=font_size)

    return hand_cursor

def buttonWin_Display(button: Button, mouse_pos: Vect2d, ) -> None:
    """Affichage du texte de fin"""

    min_size = max(button.size.x, button.size.y)

    font_size = min_size*50/400

    Display.drawRect(Vect2d(0, 0), Display.size, (0, 0, 0, button.alpha))

    if button.alpha < 127:
        button.alpha += 1
    elif button.alpha < 255 and Map.game_finished:
        button.alpha += 1

    score = Map.player_infos.get("score", 0)
    tps = Map.player_infos.get("time", 0)

    Display.drawText(button.text,
                     button.pos + button.size/2,
                     color=button.color,
                     size=font_size)

    Display.drawText("Score : " + str(score),
                     button.pos + button.size/2 + Vect2d(0, button.size.y),
                     color=button.color,
                     size=font_size)

    Display.drawText("Temps : " + str(tps) + " secondes",
                     button.pos + button.size/2 + Vect2d(0, button.size.y*2),
                     color=button.color,
                     size=font_size)
