from enum import Enum, unique
# Permet de faire des énumérations

@unique
class GameState(Enum):
    """Énumération des différents états du jeu
    Chaque état doit avoir une valeur différente

    Attributs:
        MENU: au démarrage, le menu
        GAME: le jeu en lui-même
        END: fin du jeu
        WIN: victoire
    """

    MENU = 0
    GAME = 1
    END = 2
    WIN = 3
