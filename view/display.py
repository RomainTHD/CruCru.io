import pygame
import pygame.gfxdraw
import time

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.color import Color
from util.vector import Vect2d

from view.camera import Camera

class Display:
    """Classe statique gérant l'affichage de la fenêtre

    Attributs:
        # TODO:
    """

    def __init__(self):
        """Constructeur
        La classe étant statique, une exception est levée en cas d'instanciation

        Raises:
            RuntimeError: en cas d'instanciation
        """

        raise RuntimeError("Classe statique")

    @classmethod
    def init(cls,
             width: int = 1920,
             height: int = 1080,
             fullscreen: bool = False,
             framerate: int = 60) -> (int, int):
        """Initialisation de l'affichage

        Args:
            width (int): largeur de la fenêtre
            height (int): hauteur de la fenêtre
            fullscreen (bool): plein écran ou non
            frameRate (int): nombre d'images par seconde
        """

        #! infoObject = pygame.display.Info()
        #! pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
        #! taille écran

        cls.framerate = framerate

        cls.clock = pygame.time.Clock()

        cls.frame_time = 1/framerate

        if fullscreen:
            cls.width, cls.height = pygame.display.get_surface().get_size()
        else:
            cls.width = width
            cls.height = height

        cls.resize(cls.width, cls.height)

        pygame.display.set_caption("Agar.io")
        # On change le titre

        cls.font = pygame.font.SysFont("comicsansms", 16)

        cls.updateFrame()
        # On actualise la fenêtre

    @classmethod
    def resize(cls, w, h):
        cls.window = pygame.display.set_mode((w, h), pygame.RESIZABLE)

        cls.width = w
        cls.height = h

        Camera.setWindowSize(w, h)

    @classmethod
    def updateFrame(cls) -> None:
        """Procédure pour mettre à jour la fenêtre"""

        pygame.display.flip()
        # On met à jour l'écran

        cls.window.fill(Color.BLACK)
        # On efface l'arrière-plan

        cls.clock.tick(cls.framerate)
        # Pour actualiser la fenêtre après un certain temps

    @classmethod
    def drawCircle(cls, pos: Vect2d, color: Color, radius: int, fill: bool = True) -> None:
        """Procédure pour afficher un cercle à l'écran

        INPUT :
            pos : Vect2d, un vecteur de positions
            color : Color, une couleur RGB
            radius : int, le rayon du cercle

        OUTPUT :
            None
        """

        pos_cam = pos - Camera.pos

        if fill:
            pygame.gfxdraw.filled_circle(cls.window, int(pos_cam.x), int(pos_cam.y), radius, color)
            # Dessine un cercle plein

        pygame.gfxdraw.aacircle(cls.window, int(pos_cam.x), int(pos_cam.y), radius, color)
        # Dessine un cercle vide MAIS étant soumis à l'anti-aliasing, permettant
        # un rendu plus lisse

    @classmethod
    def drawText(cls, text_str:str, pos:Vect2d, color:Color=Color.WHITE, size=None) -> None:
        """
        Procédure pour afficher du texte à l'écran

        INPUT :
            text_str : str, texte à afficher
            pos : Vect2d, position du texte
            color : Color, couleur du texte, blanc par défaut
            size : non utilisé

        OUTPUT :
            None
        """

        #! TODO: taille

        pos_cam = pos - Camera.pos

        text_str = str(text_str)

        text = cls.font.render(text_str, True, color)
        cls.window.blit(text, (int(pos_cam.x)-text.get_width()//2, int(pos_cam.y)-text.get_height()//2))

    @classmethod
    def drawLine(cls, pos1:Vect2d, pos2:Vect2d, color:Color=Color.RED, width:int=1):
        pos1_cam = pos1 - Camera.pos
        pos2_cam = pos2 - Camera.pos

        pygame.draw.line(cls.window, color, (pos1_cam.x, pos1_cam.y), (pos2_cam.x, pos2_cam.y), width)

if __name__ == "__main__":
    import time

    pygame.init()

    print("Init")
    Display.init(width=1920, height=1080, fullscreen=False, framerate=60)

    print("Cercle")
    Display.drawCircle(Vect2d(100, 100), Color.RED, radius=50)

    print("Texte")
    Display.drawText("Test", Vect2d(800, 600))

    print("Ligne")
    Display.drawLine(Vect2d(200, 300), Vect2d(400, 500), Color.BLUE)

    print("Update 1")
    Display.updateFrame()

    print("Délai 1")
    time.sleep(1)

    print("Update 2")
    Display.updateFrame()

    print("Délai 2")
    time.sleep(1)

    pygame.quit()
