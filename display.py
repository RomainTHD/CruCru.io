import pygame
import time

from color import Color
from vector import Vect2d

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
            (int, int), largeur et hauteur de la fenêtre 
        """

        #! infoObject = pygame.display.Info()
        #! pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
        #! taille écran

        cls.framerate = framerate

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

        return (cls.width, cls.height)

    @classmethod
    def updateFrame(cls) -> None:
        """
        Procédure pour mettre à jour la fenêtre
        
        INPUT :
            None
        
        OUTPUT :
            None
        """
        
        time.sleep(1/cls.framerate)
        # Pour actualiser la fenêtre après un certain temps

        pygame.display.flip()
        # On met à jour l'écran

        cls.window.fill(Color.BLACK)
        # On efface l'arrière-plan

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
        
        pygame.draw.circle(cls.window, color, (int(pos.x), int(pos.y)), radius)

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
        
        text = cls.font.render(text_str, True, color)
        cls.window.blit(text, (int(pos.x)-text.get_width()//2, int(pos.y)-text.get_height()//2))

#! rectangle = pygame.Rect(50, 50, 100, 100)
#! pygame.draw.rect(window, red, rectangle)
#! On crée un objet rectangle en (x=50, y=50) de largeur 100 et de hauteur 100
#! ici c'est donc un carré
#! la coordonnée (50, 50) correspond au coin en haut à gauche
