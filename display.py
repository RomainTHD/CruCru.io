import pygame
import time

from color import Color

class Display:
    @classmethod
    def init(cls, width:int=1920, height:int=1080, fullscreen:bool=False) -> (int, int):
        """

        """

        #! infoObject = pygame.display.Info()
        #! pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
        #! taille écran

        cls.framerate = 100

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
        time.sleep(1/cls.framerate)
        # Pour actualiser la fenêtre tous les centième de seconde

        pygame.display.flip()
        # On met à jour l'écran

        cls.window.fill(Color.BLACK)
        # On efface l'arrière-plan

    @classmethod
    def drawCircle(cls, x:int, y:int, color:Color, radius:int) -> None:
        pygame.draw.circle(cls.window, color, (int(x), int(y)), radius)

    @classmethod
    def drawText(cls, text_str:str, x:int, y:int, color:Color=Color.WHITE, size=None) -> None:
        text = cls.font.render(text_str, True, color)
        cls.window.blit(text, (int(x)-text.get_width()//2, int(y)-text.get_height()//2))

# rectangle = pygame.Rect(50, 50, 100, 100)
# pygame.draw.rect(window, red, rectangle)
# On crée un objet rectangle en (x=50, y=50) de largeur 100 et de hauteur 100
# ici c'est donc un carré
# la coordonnée (50, 50) correspond au coin en haut à gauche
