"""Programme principal à exécuter, contient les initialisations"""

import sys

if (sys.version_info[0], sys.version_info[1]) < (3, 5):
    raise Exception("Python 3.6 au moins demandé")

#! Commentaires débug, à retirer pour la version finale

import pygame
# Librairie graphique

from game.map import Map
# Terrain de jeu

from game.game import Game
# Jeu en général

from game.menu import Menu
# Menu

from game.gamestate import GameState

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
config.NB_ENEMIES
config.MAX_CELLS
config.NB_CELL_PER_SECOND
config.DELTA_T_NEW_CELL

# Test que toutes les variables de configuration existent

pygame.init()
# Initialisation de pygame

Camera.init()
# Initialisation de la caméra

Display.init(width=config.WINDOW_WIDTH,
             height=config.WINDOW_HEIGHT,
             start_fullscreen=config.START_FULLSCREEN,
             framerate=config.FRAMERATE)
# Initialisation de la fenêtre

Menu.applyState(GameState.MENU)
# Initialisation du menu

Skins.init()
# Initialisation et chargement des skins

Map.init(width=config.MAP_WIDTH,
         height=config.MAP_HEIGHT)
# Initialisation du terrain de jeu

Game.run()
# Lancement du jeu

pygame.quit()
# Fermeture de pygame
