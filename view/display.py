import pygame
import time

from util.color import Color
from util.vector import Vect2d

from view.camera import Camera

class Display:
    @classmethod
    def init(cls, width:int=1920, height:int=1080, fullscreen:bool=False, framerate:int=60) -> (int, int):
        """
        Initialisation de l'affichage

        INPUT :
            width : int, largeur de la fenêtre
            height : int, hauteur de la fenêtre
            fullscreen : bool, plein écran ou non
            frameRate : int, nombre d'images par seconde

        OUTPUT :
            dim : (int, int), largeur et hauteur de la fenêtre
        """

        #! infoObject = pygame.display.Info()
        #! pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
        #! taille écran

        cls.framerate = framerate

        cls.clock = pygame.time.Clock()

        cls.frame_time = 1/framerate

        if fullscreen:
            cls.window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            cls.width, cls.height = pygame.display.get_surface().get_size()
        else:
            cls.width = width
            cls.height = height
            cls.window = pygame.display.set_mode((cls.width, cls.height))

        pygame.display.set_caption("Agar.io")
        # On change le titre

        cls.font = pygame.font.SysFont("comicsansms", 16)

        cls.updateFrame()
        # On actualise la fenêtre

        dim = (cls.width, cls.height)

        return dim

    @classmethod
    def updateFrame(cls) -> None:
        """
        Procédure pour mettre à jour la fenêtre

        INPUT :
            None

        OUTPUT :
            None
        """

        pygame.display.flip()
        # On met à jour l'écran

        cls.window.fill(Color.BLACK)
        # On efface l'arrière-plan

        cls.clock.tick(cls.framerate)
        # Pour actualiser la fenêtre après un certain temps

    @classmethod
    def drawCircle(cls, pos:Vect2d, color:Color, radius:int) -> None:
        """
        Procédure pour afficher un cercle à l'écran

        INPUT :
            pos : Vect2d, un vecteur de positions
            color : Color, une couleur RGB
            radius : int, le rayon du cercle

        OUTPUT :
            None
        """

        pos_cam = pos - Camera.pos

        pygame.draw.circle(cls.window, color, (int(pos_cam.x), int(pos_cam.y)), radius)

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

        pos_cam = pos - Camera.pos

        text_str = str(text_str)

        text = cls.font.render(text_str, True, color)
        cls.window.blit(text, (int(pos_cam.x)-text.get_width()//2, int(pos_cam.y)-text.get_height()//2))

    @classmethod
    def drawLine(cls, pos1:Vect2d, pos2:Vect2d, color:Color=Color.RED, width:int=1):
        pos1_cam = pos1 - Camera.pos
        pos2_cam = pos2 - Camera.pos

        pygame.draw.line(cls.window, color, (pos1_cam.x, pos1_cam.y), (pos2_cam.x, pos2_cam.y), width)

#! rectangle = pygame.Rect(50, 50, 100, 100)
#! pygame.draw.rect(window, red, rectangle)
#! On crée un objet rectangle en (x=50, y=50) de largeur 100 et de hauteur 100
#! ici c'est donc un carré
#! la coordonnée (50, 50) correspond au coin en haut à gauche
