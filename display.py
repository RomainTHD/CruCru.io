import pygame
import time

from map import Map
from color import Color

class Display:
    @classmethod
    def init(cls, width, height):
        cls.width = width
        cls.height = height
        # Largeur et hauteur de la fenêtre

        cls.window = pygame.display.set_mode((cls.width, cls.height))

        pygame.display.set_caption("Agar.io")
        # On change le titre

        cls.updateFrame()
        # On actualise la fenêtre

    @classmethod
    def updateFrame(cls):
        time.sleep(1/100)
        # Pour actualiser la fenêtre tous les centième de seconde

        pygame.display.flip()
        # On met à jour l'écran

        cls.window.fill(Color.black)
        # On efface l'arrière-plan

    @classmethod
    def drawCircle(cls, x, y, color, radius):
        pygame.draw.circle(cls.window, color, (int(x), int(y)), radius)






# rectangle = pygame.Rect(50, 50, 100, 100)
# pygame.draw.rect(window, red, rectangle)
# On crée un objet rectangle en (x=50, y=50) de largeur 100 et de hauteur 100
# ici c'est donc un carré
# la coordonnée (50, 50) correspond au coin en haut à gauche
