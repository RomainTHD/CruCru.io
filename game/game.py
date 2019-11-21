"""Partie principale du jeu"""

import pygame

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from game.map import Map
from game.menu import Menu
from game.gamestate import GameState

from util.vector import Vect2d

from view.display import Display

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

        cls.state = GameState.MENU

        while not cls.finished:
            cls.ESC_MAX_FRAMECOUNT = Display.real_framerate*0.25

            cls.handleKeys()

            mx, my = pygame.mouse.get_pos()
            mouse_pos = Vect2d(mx, my)
            # Position de la souris

            mouse_pressed = pygame.mouse.get_pressed()[0]

            Menu.state = GameState.MENU

            if cls.state == GameState.MENU:
                Menu.update(mouse_pos, mouse_pressed)

                if Menu.can_play:
                    cls.state = GameState.GAME

                if Menu.can_quit:
                    cls.finished = True

                Menu.display()

                if Menu.can_play:
                    Display.setCursorArrow()

            elif cls.state == GameState.END:
                Menu.update(mouse_pos, mouse_pressed)

                if not Map.game_finished:
                    Map.update()

                if Menu.can_play:
                    cls.state = GameState.GAME

                if Menu.can_quit:
                    cls.finished = True

                Map.display()
                Menu.display()

                if Menu.can_play:
                    Display.setCursorArrow()
            elif cls.state == GameState.WIN:
                Menu.update(mouse_pos, mouse_pressed)

                if Menu.can_play:
                    cls.state = GameState.GAME

                if Menu.can_quit:
                    cls.finished = True

                Menu.display()

                if Menu.can_play:
                    Display.setCursorArrow()
            elif cls.state == GameState.GAME:
                Map.setMousePos(mouse_pos/Display.zoom_factor)
                Map.update()
                Map.display()

                if Map.isPlayerAlive():
                    if Map.game_finished:
                        cls.state = GameState.WIN
                        Menu.applyState(GameState.WIN)
                else:
                    cls.state = GameState.END
                    Menu.applyState(GameState.END)
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

        if keys[pygame.K_RETURN]:
            for k in Map.creatures.keys():
                if k != Map.player_id:
                    for enemy in Map.creatures[k]:
                        enemy.score += 100

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

                if event.key == pygame.K_SPACE:
                    Map.splitPlayer()
