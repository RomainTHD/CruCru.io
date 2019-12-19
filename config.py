"""Variables de configuration du programme"""

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# Largeur et hauteur de la fenêtre

FRAMERATE = 120
# Images par seconde

MAP_WIDTH = 2000
MAP_HEIGHT = 2000
# Largeur et hauteur de la map

GRID_WIDTH = 10
GRID_HEIGHT = 10
# Nombre de cases sur la map. Utilisé pour les hitbox et l'affichage

NB_ENEMIES = 5
# Nombre d'ennemis sur la map (sans compter les split)

MAX_CELLS = 4000
# Nombre maximal de cellules sur la map

NB_CELL_PER_SECOND = 50
DELTA_T_NEW_CELL = 0.1

SPEED_COEFF = 700
# Vitesse des créatures

SPEED_SIZE_POWER = 0.1
# Accélération relative à la taille
# > 0 : décélère avec la taille
# 0 : vitesse constante
# < 0 : accélère avec la taille

MAX_SPLIT = 4
# Nombre maximal d'enfants au total pour le split

RADIUS_POWER_SCORE = 0.65
# Taux de grossissement des créatures en fonction de leur score

SPLIT_TIME = 5
# Temps d'invincibilité relative à sa propre famille d'une créature

NB_BUSHES = 1
# Nombre de buissons

ALLOW_SKINS = True
