#! commentaires débug

import pygame

from game.map import Map

from entity.player import Player

from util.color import Color
from util.vector import Vect2d

from view.display import Display
from view.camera import Camera

import config

pygame.init()
# On initialise pygame

w, h = Display.init(fullscreen=config.IS_FULLSCREEN,
                    width=config.WINDOW_WIDTH,
                    height=config.WINDOW_HEIGHT,
                    framerate=config.FRAMERATE)
# On initialise la fenêtre

Map.init(config.MAP_WIDTH, config.MAP_HEIGHT, framerate=Display.framerate)
# On initialise le terrain de jeu
# Pour l'instant il a la même taille que la fenêtre

Camera.setWindowSize(w, h)

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

    mx, my = pygame.mouse.get_pos()
    # Position (x, y) de la souris

    if not pygame.mouse.get_focused():
        # Si souris hors de la fenêtre
        # print("out")
        pass


    Map.player.mouse_pos = Vect2d(mx, my) - Vect2d(Display.width/2, Display.height/2)
    Map.update()
    Map.display()

    Camera.setPos(Map.player.pos)

    Display.updateFrame()

pygame.quit()
