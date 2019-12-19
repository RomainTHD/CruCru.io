"""Ennemi"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")

import math
import random
import time

from util.vector import Vect2d

from entity.creature import Creature

class Enemy(Creature):
    """Ennemi, hérite de Creature

    Attributs:
        cf. Creature

        map_cell (list of list of Vect2d):
        creature_info (list of Vect2d and int):
        speed (Vect2d)
    """

    def __init__(self, pos: Vect2d, name: str, color: 'Color', creature_id: int) -> None:
        """Constructeur

        Args:
            pos (Vect2d): position du centre de l'ennemi
            name (str): nom de l'ennemi
            color (Color): couleur de l'ennemi
            creature_id (int): id de la famille de la créature
        """

        super().__init__(pos, name, color, creature_id)

        self.map_cell = None
        self.creatures_info = None

        self.speed = Vect2d(random.random()*2-1, random.random()*2-1)
        # Vitesse initiale

    def setMapCell(self, map_cell: list) -> None:
        self.map_cell = map_cell

    def searchCellDest(self, radius: int, map_size: Vect2d) -> None:
        maxi = 0
        liste_pos_maxi = []

        score = 0

        grid_size = Vect2d(len(self.map_cell), len(self.map_cell[0]))

        map_pos = self.getMapPos(map_size, grid_size)

        for x in range(map_pos.x-radius, map_pos.x+radius+1):
            for y in range(map_pos.y-radius, map_pos.y+radius+1):
                if x in range(grid_size.x) and y in range(grid_size.y):
                    taille = len(self.map_cell[x][y])

                    if taille == maxi:
                        liste_pos_maxi += [(x, y)]
                    elif taille > maxi:
                        maxi = taille
                        liste_pos_maxi = [(x, y)]

        distance_mini = float("inf")
        coords_mini = None

        for x, y in liste_pos_maxi:
            for j in range(len(self.map_cell[x][y])):
                pos = self.map_cell[x][y][j]

                dist = Vect2d.dist(pos, self.pos)

                if dist < distance_mini:
                    score = len(self.map_cell[x][y])
                    distance_mini = dist
                    coords_mini = self.map_cell[x][y][j]

        return coords_mini, score

    def setCreaturesInfo(self, creatures_info: list) -> None:
        self.creatures_info = creatures_info

    def speedEnemies(self, map_size: Vect2d) -> tuple:
        dist_target = float("inf")
        dist_hunter = float("inf")

        speed_target = None
        speed_hunter = None

        can_split = False

        score_target = None

        for enemy_pos, enemy_radius, enemy_score in self.creatures_info:
            dist = Vect2d.dist(self.pos, enemy_pos) - self.radius - enemy_radius

            if Creature.canEat(enemy_score, self.score):
                if dist < dist_hunter:
                    speed_hunter = enemy_pos - self.pos
                    dist_hunter = dist

            elif Creature.canEat(self.score, enemy_score):
                if dist < dist_target:
                    speed_target = enemy_pos - self.pos
                    dist_target = dist
                    score_target = enemy_score

        if score_target is not None:
            if score_target < self.score//2:
                if dist_target > self.radius and dist_target < self.radius*2:
                    can_split = True

        if speed_hunter is None:
            speed_hunter = Vect2d(0, 0)

        if speed_target is None:
            speed_target = Vect2d(0, 0)

        coeff_target = 1 - dist_target/map_size.length()
        coeff_target = abs(coeff_target**3)

        if coeff_target == float("inf"):
            coeff_target = 0
        elif coeff_target >= 1:
            coeff_target = 1

        coeff_target = coeff_target if coeff_target != float("inf") else 0

        coeff_hunter = 1 - dist_hunter/map_size.length()
        coeff_hunter = abs(coeff_hunter**3)

        if coeff_hunter == float("inf"):
            coeff_hunter = 0
        elif coeff_hunter >= 1:
            coeff_hunter = 1

        return speed_target, coeff_target, speed_hunter, coeff_hunter, can_split

    def update(self, map_size: Vect2d) -> None:
        grid_size = Vect2d(len(self.map_cell), len(self.map_cell[0]))

        max_radius = grid_size.x
        radius = 1
        speed_cell = None
        cell_score = 0
        can_split = False

        while speed_cell is None and radius < max_radius:
            speed_cell, cell_score = self.searchCellDest(radius, map_size)
            radius += 1

        if speed_cell is None:
            speed_cell = Vect2d(0, 0)
        else:
            speed_cell = speed_cell - self.pos

        speed_target, coeff_target, speed_hunter, coeff_hunter, can_split = self.speedEnemies(map_size)

        bords = [Vect2d(self.pos.x, self.radius),
                 Vect2d(self.pos.x, map_size.y-self.radius),
                 Vect2d(self.radius, self.pos.y),
                 Vect2d(map_size.x-self.radius, self.pos.y)]

        coeff_bords = []

        for bord in bords:
            dist_bord = Vect2d.dist(bord, self.pos)
            coeff_bord = math.exp(-(dist_bord**0.2)/2)**3
            coeff_bord = coeff_bord if coeff_bord <= 1 else 0
            coeff_bords.append(coeff_bord)

        speed_family = Vect2d(0, 0)

        coeff_family = 0
        taille = 0

        for creature in self.family:
            if self is not creature:
                taille += 1

                coeff = (time.time() - creature.invincibility_family_time)/self.SPLIT_TIME

                if coeff > 1:
                    coeff = 1

                coeff = coeff ** 3
                coeff_family += coeff
                speed_family += (creature.pos - self.pos)*coeff

        self.speed *= 0.98 + self.inertia

        if taille != 0:
            coeff_family /= taille

        direction = (speed_cell*(1-coeff_target)*(1-coeff_hunter)*(1-coeff_family)).normalize()\
                  + (speed_target*coeff_target*(1-coeff_hunter)*(1-coeff_family)).normalize()\
                  - (speed_hunter*(1-coeff_target)*coeff_hunter*(1-coeff_family)).normalize()\
                  + (speed_family*coeff_target*(1-coeff_hunter)*coeff_family).normalize()

        if can_split:
            if self.speed != Vect2d(0, 0) and speed_target != Vect2d(0, 0):
                angle = Vect2d.angleBetween(self.speed, speed_target)

                if abs(angle) < 10:
                    self.split()

        self.speed += direction

        self.speed.x -= 1 * coeff_bords[0] * self.speed.y
        self.speed.y += 1 * coeff_bords[0] * abs(self.speed.y)

        self.speed.x -= 1 * coeff_bords[1] * self.speed.y
        self.speed.y -= 1 * coeff_bords[1] * abs(self.speed.y)

        self.speed.y += 1 * coeff_bords[2] * self.speed.x
        self.speed.x += 1 * coeff_bords[2] * abs(self.speed.x)

        self.speed.y += 1 * coeff_bords[3] * self.speed.x
        self.speed.x -= 1 * coeff_bords[3] * abs(self.speed.x)

        self.direction = self.speed.normalize()

        self.applySpeed(map_size)
