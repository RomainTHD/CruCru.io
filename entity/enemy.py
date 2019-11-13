"""Ennemi"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")

import math
import random

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

    def __init__(self, pos, name, color, id) -> None:
        super().__init__(pos, name, color, id)

        self.map_cell = None
        self.creatures_info = None

        self.speed = Vect2d(random.random()*2-1, random.random()*2-1)

        #!
        """
        self.pos = Vect2d(1000, 1000)
        self.speed = Vect2d(0, -1)
        """

    def setMapCell(self, map_cell):
        self.map_cell = map_cell

    def searchCellDest(self, radius, map_size):
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

    def setCreaturesInfo(self, creatures_info: list):
        self.creatures_info = creatures_info

    def speedEnemies(self, map_size: Vect2d):
        dist_target = float("inf")
        dist_hunter = float("inf")

        speed_target = None
        speed_hunter = None

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

        return speed_target, coeff_target, speed_hunter, coeff_hunter

    def update(self, map_size):
        grid_size = Vect2d(len(self.map_cell), len(self.map_cell[0]))

        max_radius = grid_size.x
        radius = 1
        speed_cell = None
        cell_score = 0

        while speed_cell is None and radius < max_radius:
            speed_cell, cell_score = self.searchCellDest(radius, map_size)
            radius += 1

        if speed_cell is None:
            speed_cell = Vect2d(0, 0)
        else:
            speed_cell = speed_cell - self.pos

        speed_target, coeff_target, speed_hunter, coeff_hunter = self.speedEnemies(map_size)

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

        #!
        """
        for i in range(4):
            print(int(coeff_bords[i]*100)/100, end=', ')

        print(self.speed)
        """

        self.speed *= 0.98

        self.speed += speed_cell*(1-coeff_target)*(1-coeff_hunter)
        self.speed += speed_target*coeff_target*(1-coeff_hunter)
        self.speed -= speed_hunter*(1-coeff_target)*coeff_hunter

        self.speed.x -= 0.1 * coeff_bords[0] * self.speed.y
        self.speed.y += 0.1 * coeff_bords[0] * abs(self.speed.y) + 1

        self.speed.x -= 0.1 * coeff_bords[1] * self.speed.y
        self.speed.y -= 0.1 * coeff_bords[1] * abs(self.speed.y) + 1

        self.speed.y += 0.1 * coeff_bords[2] * self.speed.x
        self.speed.x += 0.1 * coeff_bords[2] * abs(self.speed.x) + 1

        self.speed.y += 0.1 * coeff_bords[3] * self.speed.x
        self.speed.x -= 0.1 * coeff_bords[3] * abs(self.speed.x) + 1

        self.direction = self.speed.normalize()

        self.applySpeed(map_size)
