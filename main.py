"""Programme principal à exécuter, contient les initialisations"""

#! Commentaires débug, à retirer pour la version finale

import pygame
# Librairie graphique

from game.map import Map
# Terrain de jeu

from game.game import Game
# Jeu en général

from game.menu import Menu
# Menu

from view.display import Display
# Fenêtre

from view.camera import Camera
# Caméra

from view.skins import Skins
# Skins

import config
# Variables de configuration

config.WINDOW_WIDTH
config.WINDOW_HEIGHT
config.FRAMERATE
config.MAP_WIDTH
config.MAP_HEIGHT
config.START_FULLSCREEN
config.DEBUG
# Test que toutes les variables de configuration existent

pygame.init()
# Initialisation de pygame

Display.init(width=config.WINDOW_WIDTH,
             height=config.WINDOW_HEIGHT,
             start_fullscreen=config.START_FULLSCREEN,
             framerate=config.FRAMERATE)
# Initialisation de la fenêtre

Camera.init()
# Initialisation de la caméra

Skins.init()
# Initialisation et chargement des skins

Map.init(width=config.MAP_WIDTH,
         height=config.MAP_HEIGHT)
# Initialisation du terrain de jeu

Menu.init()
# Initialisation du menu

Game.run()
# Lancement du jeu

pygame.quit()
# Fermeture de pygame
