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
        BASE_RADIUS (int)
        BASE_SCORE (int)
        BASE_PERCENT (int):
        SPEED_COEFF (int):
        SPEED_SIZE_POWER (int):

        pos (Vect2d):
        radius (int):
        score (int):
        name (str):
        color (Color):
        creature_id (int):
        is_alive (bool):
        img (pygame.Surface):
    """

    BASE_RADIUS = 20
    BASE_PERCENT = 10/100
    BASE_SCORE = 10
    SPEED_COEFF = config.SPEED_COEFF
    SPEED_SIZE_POWER = config.SPEED_SIZE_POWER
    RADIUS_POWER_SCORE = config.RADIUS_POWER_SCORE
    SPLIT_TIME = config.SPLIT_TIME

    def __init__(self, pos: Vect2d, name: str, color: Color, creature_id: int):
        """Constructeur

        Args:
            pos (Vect2d): position de la créature
            name (str): nom de la créature
        """

        self.family = [self]

        self.invincibility_family_time = time.time()

        self.pos = pos.copy()

        self.radius = self.BASE_RADIUS

        self.score = Creature.BASE_SCORE

        self.name = name

        self.color = color
        self.opposite_color = Color.oppositeColor(color)

        self.creature_id = creature_id
        self.killer_id = None

        self.is_alive = True

        self.img = Skins.getRandomSkin()

        self.split_speed = 0

        self.inertia = 0

        self.speed = Vect2d(0, 0)
        self.direction = Vect2d(0, 0)

    def getMapPos(self, size: Vect2d, grid_size: Vect2d):
        """

        """

        pos_x = int(self.pos.x/size.x * grid_size.x)
        pos_y = int(self.pos.y/size.y * grid_size.y)

        return Vect2d(pos_x, pos_y)

    @abstractmethod
    def update(self, size):
        raise NotImplementedError("Cette méthode doit être définie")

    @staticmethod
    def canEat(radius, other_radius):
        area = 2*math.pi*radius**2
        other_area = 2*math.pi*other_radius**2

        return area > other_area*(1+Creature.BASE_PERCENT)

    def display(self) -> None:
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

        if config.DEBUG:
            txt = self.score
        else:
            txt = self.name

        Display.drawText(text=txt,
                         size=self.radius*0.75,
                         color=self.opposite_color,
                         pos=self.pos,
                         base_pos=Camera.pos)

    def applySpeed(self, size):
        self.direction = self.direction*self.SPEED_COEFF*(1+self.split_speed)/Display.real_framerate

        self.split_speed *= 0.98
        self.inertia *= 0.99

        area = 2*math.pi*self.radius**2

        self.direction *= area**(-self.SPEED_SIZE_POWER)

        new_pos = self.pos + self.direction

        if new_pos.x > self.radius and new_pos.x < size.x-self.radius:
            self.pos.x = new_pos.x

        if new_pos.y > self.radius and new_pos.y < size.y-self.radius:
            self.pos.y = new_pos.y

        while self.pos.x < self.radius:
            self.pos.x += 1

        while self.pos.x > size.x-self.radius:
            self.pos.x -= 1

        while self.pos.y < self.radius:
            self.pos.y += 1

        while self.pos.y > size.y-self.radius:
            self.pos.y -= 1

        r = self.radiusFormula()

        self.radius += (r - self.radius)/10

    def radiusFormula(self):
        return round(self.BASE_RADIUS + 2*self.score**self.RADIUS_POWER_SCORE)

    def kill(self, score: int):
        self.score += score

    def killed(self, killer_id: int):
        self.is_alive = False
        self.killer_id = killer_id

    @classmethod
    def notifyMapNewCreature(cls, parent, is_player, override_limit):
        raise NotImplementedError("Est supposé être réécrit par Map")

    def split(self, is_player=False, override_limit=False):
        if self.score > Creature.BASE_SCORE*3:
            Creature.notifyMapNewCreature(self, is_player, override_limit)
