if __name__ == "__main__":
    import sys
    sys.path.append("..")

import pygame

from game.map import Map

from util.vector import Vect2d

from view.display import Display
from view.camera import Camera

class Game:
    @classmethod
    def run(cls):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    # Détection de la fermeture de la fenêtre

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        # Détection de la touche échap

                if event.type == pygame.VIDEORESIZE:
                    Display.resize(event.w, event.h)

            mx, my = pygame.mouse.get_pos()
            # Position (x, y) de la souris

            if not pygame.mouse.get_focused():
                # Si souris hors de la fenêtre
                #!
                pass

            Map.player.mouse_pos = Vect2d(mx, my) - Vect2d(Display.width/2, Display.height/2)
            Map.update()
            Map.display()

            Camera.setPos(Map.player.pos)

            Display.updateFrame()
