"""Programme principal à exécuter, contient les initialisations"""

import sys

if (sys.version_info[0], sys.version_info[1]) < (3, 5):
    # Vérification de la version de Python
    raise Exception("Python 3.6 au moins demandé")

import pygame
# Librairie graphique

import config
# Variables de configuration

config.WINDOW_WIDTH
config.WINDOW_HEIGHT
config.FRAMERATE
config.MAP_WIDTH
config.MAP_HEIGHT
config.START_FULLSCREEN
config.DEBUG
config.MAX_CREATURES
config.MAX_CELLS
config.NB_CELL_PER_SECOND
config.DELTA_T_NEW_CELL
config.SPEED_COEFF
config.SPEED_SIZE_POWER
config.MAX_SPLIT
config.RADIUS_POWER_SCORE
config.SPLIT_TIME
# Test que toutes les variables de configuration existent

from game.map import Map
# Terrain de jeu

from game.game import Game
# Jeu en général

from game.menu import Menu
# Menu

from game.gamestate import GameState
# États du jeu

from view.display import Display
# Fenêtre

from view.camera import Camera
# Caméra

from view.skins import Skins
# Skins

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
