"""Partie principale du jeu"""

from enum import Enum, unique
# Permet de faire des énumérations

import pygame

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from game.map import Map

from game.menu import Menu

from util.vector import Vect2d

from view.display import Display
from view.camera import Camera

@unique
class GameState(Enum):
    """Énumération des différents états du jeu
    Chaque état doit avoir une valeur différente

    États :
        MENU : au démarrage, le menu
        GAME : le jeu en lui-même
        END : fin du jeu
    """

    MENU = 0
    GAME = 1
    END = 2

class Game:
    """Gestion du jeu

    Attributs:
        run (bool): condition d'arrêt de la boucle de jeu
        keytime (dict): nombre d'images où une touche est enfoncée
        ESC_MAX_FRAMECOUNT (float): nombre maximal d'images où la touche ESC doit être enfoncée pour
                                    quitter le jeu
        state (GameState): état du jeu
    """

    finished: bool
    keytime: dict
    ESC_MAX_FRAMECOUNT: float
    state: GameState

    @classmethod
    def run(cls) -> None:
        """Méthode principale permettant de faire tourner le jeu"""

        cls.finished = False

        cls.keytime = {}

        cls.ESC_MAX_FRAMECOUNT = Display.framerate*0.25

        cls.state = GameState.MENU

        while not cls.finished:
            cls.handleKeys()

            mx, my = pygame.mouse.get_pos()
            mouse_pos = Vect2d(mx, my)
            # Position de la souris

            mouse_pressed = pygame.mouse.get_pressed()[0]

            if cls.state == GameState.MENU:
                Menu.update(mouse_pos, mouse_pressed)
                Menu.display()

                if Menu.can_play:
                    cls.state = GameState.GAME
            elif cls.state == GameState.GAME:
                Map.setMousePos(mouse_pos)
                Map.update()
                Map.display()

                Camera.setPos(Map.player.pos)
            else:
                raise ValueError("État inconnu")

            alpha = cls.keytime.get(pygame.K_ESCAPE, 0)/cls.ESC_MAX_FRAMECOUNT*255

            Display.drawText("Quitter...",
                             Vect2d(50, 25),
                             color=(255, 0, 0, alpha),
                             size=16,
                             base_pos=Vect2d(0, 0))

            Display.updateFrame()

    @classmethod
    def handleKeys(cls) -> None:
        """Méthode permettant de traiter les entrées clavier"""

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            # Si la touche ESC est pressée

            if cls.keytime.get(pygame.K_ESCAPE, 0) > cls.ESC_MAX_FRAMECOUNT:
                # Si l'on est au dessus de la valeur maximale pour quitter
                cls.finished = True
            else:
                cls.keytime[pygame.K_ESCAPE] = cls.keytime.get(pygame.K_ESCAPE, 0) + 1
                # Sinon on incrémente le nombre d'images écoulées
        else:
            cls.keytime[pygame.K_ESCAPE] = 0
            # Si elle est relachée on remet le compteur à 0

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                # Quand la fenêtre est redimensionnée
                Display.resize(event.w, event.h)

            if event.type == pygame.QUIT:
                # Détection de la fermeture de la fenêtre
                cls.finished = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    # Quand F11 on se met en plein écran
                    Display.toggleFullscreen()
