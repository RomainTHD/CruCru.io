"""Programme principal à exécuter"""

#! Commentaires débug, à retirer pour la version finale

import pygame
# Librairie graphique

from game.map import Map
# Terrain de jeu

from game.game import Game
# Jeu en général

from game.menu import Menu

from view.display import Display
# Fenêtre

import config
# Variables de configuration

pygame.init()
# Initialisation de pygame

Display.init(width=config.WINDOW_WIDTH,
             height=config.WINDOW_HEIGHT,
             fullscreen=config.IS_FULLSCREEN,
             framerate=config.FRAMERATE)
# Initialisation de la fenêtre

Map.init(config.MAP_WIDTH, config.MAP_HEIGHT, framerate=Display.framerate)
# Initialisation du terrain de jeu

Menu.init(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

Game.run()
# Lancement du jeu

pygame.quit()
# Fermeture de pygame
