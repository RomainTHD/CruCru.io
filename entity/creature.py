"""Créature générique"""

import math

import time

from abc import ABC, abstractmethod
# Permet de forcer l'implémentation d'une méthode

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.vector import Vect2d
from util.color import Color

from view.camera import Camera
from view.display import Display
from view.skins import Skins

import config

class Creature(ABC):
    """Créature générique
    Classe mère des créatures Enemy et Player

    Attributs:
        BASE_RADIUS (int): rayon lorsque le score est de 0
        BASE_PERCENT (float): différence d'aire requise pour manger une créature
        BASE_SCORE (int): score initial d'une créature
        SPEED_COEFF (int): vitesse
        SPEED_SIZE_POWER (float): coefficient de vitesse selon la taille
        RADIUS_POWER_SCORE (float): coefficient de rayon selon le score
        SPLIT_TIME (int): temps d'invincibilité avec sa propre famille pour le split

        family (list): créatures de la même famille
        invincibility_family_time (float): temps depuis la création
        creature_id (int): id de la famille de la créature
        killer_id (int): id du tueur

        pos (Vect2d): position
        speed (Vect2d): vitesse de la créature
        direction (Vect2d): vitesse normée de la créature
        split_speed (float): boost de vitesse lors du split
        inertia (float): inertie

        radius (float): rayon
        color (Color): couleur
        opposite_color (Color): couleur opposée
        name (str): nom
        img (pygame.Surface): image affichée

        score (int): score
        is_alive (bool): vivant ou non
    """

    BASE_RADIUS = 20
    BASE_PERCENT = 10/100
    BASE_SCORE = 5
    SPEED_COEFF = config.SPEED_COEFF
    SPEED_SIZE_POWER = config.SPEED_SIZE_POWER
    RADIUS_POWER_SCORE = config.RADIUS_POWER_SCORE
    SPLIT_TIME = config.SPLIT_TIME

    def __init__(self, pos: Vect2d, name: str, color: Color, creature_id: int) -> None:
        """Constructeur

        Args:
            pos (Vect2d): position de la créature
            name (str): nom de la créature
            color (Color): couleur de la créature
            creature_id (int): id de la famille de la créature
        """

        self.family = [self]
        self.invincibility_family_time = time.time()
        self.creature_id = creature_id
        self.killer_id = None

        self.pos = pos.copy()
        self.speed = Vect2d(0, 0)
        self.direction = Vect2d(0, 0)
        self.split_speed = 0
        self.inertia = 0

        self.radius = self.BASE_RADIUS
        self.color = color
        self.opposite_color = Color.oppositeColor(color)
        self.name = name
        self.img = Skins.getRandomSkin()

        self.score = Creature.BASE_SCORE
        self.is_alive = True

    def getMapPos(self, size: Vect2d, grid_size: Vect2d) -> Vect2d:
        """Permet de translater une position absolue en position dans une grille

        Args:
            size (Vect2d): taille de l'espace d'origine
            grid_size (Vect2d): taille de l'espace d'arrivée

        Returns:
            Vect2d: les 2 positions
        """

        pos_x = int(self.pos.x/size.x * grid_size.x)
        pos_y = int(self.pos.y/size.y * grid_size.y)

        return Vect2d(pos_x, pos_y)

    @abstractmethod
    def update(self, map_size: Vect2d) -> None:
        """Met à jour la créature
        Méthode à implémenter

        Args:
            map_size (Vect2d): taille du monde
        """

        raise NotImplementedError("Cette méthode doit être définie")

    def display(self) -> None:
        """Permet d'afficher la créature"""



        #!
        """
        Display.drawImg(img=self.img,
                        pos=self.pos,
                        radius=self.radius,
                        base_pos=Camera.pos)
        """

        Display.drawCircle(pos=self.pos,
                           color=self.color,
                           radius=self.radius,
                           base_pos=Camera.pos)

        Display.drawText(text=self.name,
                         size=self.radius*0.75,
                         color=self.opposite_color,
                         pos=self.pos,
                         base_pos=Camera.pos)

    def applySpeed(self, size: Vect2d) -> None:
        """Permet de faire avancer la créature en appliquant sa vitesse

        Args:
            size (Vect2d): taille de la map
        """

        self.direction *= self.SPEED_COEFF
        # On applique à la direction la vitesse

        self.direction *= 1+self.split_speed
        # On applique le boost de vitesse dû au split

        self.direction /= Display.real_framerate
        # La vitesse de chaque créature est proportionnelle au nombre d'images
        # par seconde de la fenêtre afin d'éviter un jeu trop rapide à 120 fps
        # ou trop lent à 30 fps par exemple

        area = 2*math.pi*self.radius**2
        self.direction *= area**(-self.SPEED_SIZE_POWER)
        # On diminue la vitesse en fonction de l'aire

        self.split_speed *= 0.98
        self.inertia *= 0.99

        new_pos = self.pos + self.direction
        # On calcule la nouvelle position

        if new_pos.x > self.radius and new_pos.x < size.x-self.radius:
            # Pour éviter un effet visuel de rebond, la nouvelle position n'est
            # appliquée que si elle est correcte
            self.pos.x = new_pos.x

        if new_pos.y > self.radius and new_pos.y < size.y-self.radius:
            self.pos.y = new_pos.y

        while self.pos.x < self.radius:
            # Vérification de la position en fonction du rayon
            # le rayon va en effet changer si la créature grossit
            self.pos.x += 1

        while self.pos.x > size.x-self.radius:
            self.pos.x -= 1

        while self.pos.y < self.radius:
            self.pos.y += 1

        while self.pos.y > size.y-self.radius:
            self.pos.y -= 1

        self.radius += (Creature.radiusFormula(self.score) - self.radius)/10
        # Calcul du nouveau rayon, qui sera progressif

    @staticmethod
    def canEat(radius: float, other_radius: float) -> bool:
        """Fonction permettant de savoir si une créature A peut manger une autre
           créature B

        Args:
            radius (float): rayon de la créature A
            other_radius (float): rayon de la créature B

        Returns:
            bool: si la créature A peut manger la créature B
        """

        area = 2*math.pi*radius**2
        other_area = 2*math.pi*other_radius**2

        return area > other_area*(1+Creature.BASE_PERCENT)

    @staticmethod
    def radiusFormula(score: int) -> float:
        """Fonction permettant de calculer le rayon d'une créature en fonction
        de son score

        Args:
            score (int): score

        Returns:
            float: rayon associé au score
        """

        return Creature.BASE_RADIUS + 2*score**Creature.RADIUS_POWER_SCORE

    def kill(self, score: int) -> None:
        """Procédure exécutée lorsque cette créature en tue une autre

        Args:
            score (int): score de l'autre créature
        """

        self.score += score

    def killed(self, killer_id: int) -> None:
        """Procédure exécutée lorsque cette créature est tuée

        Args:
            killer_id (int): id de la créature ayant tué la créature
        """

        self.killer_id = killer_id
        self.is_alive = False

    @classmethod
    def notifyMapNewCreature(cls, parent: 'Creature', is_player: bool, override_limit: bool) -> None:
        """Notifie la Map qu'une nouvelle créature doit être créée

        Args:
            parent (Creature): créature parente de la nouvelle créature
            is_player (bool): si cette créature est un joueur ou non
            override_limit (bool): si les limites de nombre de créatures doivent
                                   être respéctées ou non
        """

        raise NotImplementedError("Est supposé être réécrit par Map")

    def split(self, is_player: bool = False, override_limit: bool = False) -> None:
        """Split de la créature

        Args:
            is_player (bool): si cette créature est un joueur ou non
            override_limit (bool): si les limites de nombre de créatures doivent
                                   être respéctées ou non. Elles sont respéctées
                                   dans un split normal et non respéctées lors
                                   d'un split de buisson
        """

        if self.score > Creature.BASE_SCORE*3:
            Creature.notifyMapNewCreature(self, is_player, override_limit)
