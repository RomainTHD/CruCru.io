"""Variables de configuration du programme"""

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# Largeur et hauteur de la fenêtre

FRAMERATE = 60
# Images par seconde

MAP_WIDTH = 2000
MAP_HEIGHT = 2000
# Largeur et hauteur de la map

START_FULLSCREEN = False
# Si la fenêtre est en plein écran ou non

DEBUG = False
# Mode de débogage, avec certaines informations supplémentaires affichées

MAX_CREATURES = 100
# Nombre maximal de créatures sur la map

MAX_CELLS = 1000
# Nombre maximal de cellules sur la map

NB_CELL_PER_SECOND = 20
DELTA_T_NEW_CELL = 0.1

SPEED_COEFF = 700
# Vitesse des créatures

SPEED_SIZE_POWER = 0.1
# Puissance relative à la taille
# > 0 : décélère avec la taille
# 0 : vitesse constante
# < 0 : accélère avec la taille

MAX_SPLIT = 4

RADIUS_POWER_SCORE = 0.65

SPLIT_TIME = 5
