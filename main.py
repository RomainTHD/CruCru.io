import pygame

from player import Player
from color import Color
from display import Display
from map import Map

player = Player()
# Création du joueur

pygame.init()
# On initialise pygame

Display.init(800, 600)
# On initialise la fenêtre

Map.init(800, 600)
# On initialise le terrain de jeu
# Pour l'instant il a la même taille que la fenêtre



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

    Map.creer_boule()
    Map.affiche_cellule()

    player.update(mx, my)
    player.display()

    Display.updateFrame()

pygame.quit()
