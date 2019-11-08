if __name__ == "__main__":
    raise RuntimeError("Ne peut pas être lancé seul")

import math
import random

from util.vector import Vect2d

from entity.creature import Creature

class Enemy(Creature):
    """Ennemi, hérite de Creature

    Attributs:
        cf. Creature
        map (list of list of )

    """

    def __init__(self, pos, name, color, id) -> None:
        super().__init__(pos, name, color, id)

        self.map = None
        self.creature_info = None

        self.speed = Vect2d(random.random()*2-1, random.random()*2-1)

    def searchDest(self, radius, map_size):
        maxi = 0
        liste_pos_maxi = []

        score = 0

        grille_size = Vect2d(len(self.map), len(self.map[0]))

        map_pos = self.getMapPos(map_size, grille_size)

        for x in range(map_pos.x-radius, map_pos.x+radius+1):
            for y in range(map_pos.y-radius, map_pos.y+radius+1):
                if x in range(grille_size.x) and y in range(grille_size.y):
                    taille = len(self.map[x][y])
                    # print(self.map)

                    if taille == maxi:
                        liste_pos_maxi += [(x, y)]
                    elif taille > maxi:
                        maxi = taille
                        liste_pos_maxi = [(x, y)]

        distance_mini = float("inf")
        coords_mini   = None

        for i in range(len(liste_pos_maxi)):
            x, y = liste_pos_maxi[i]

            for j in range(len(self.map[x][y])):
                pos = self.map[x][y][j]

                dist = Vect2d.dist(pos, self.pos)

                if dist < distance_mini:
                    score = len(self.map[x][y])
                    distance_mini = dist
                    coords_mini = self.map[x][y][j]

        return coords_mini, score

    def update(self, map_size):
        grille_size = Vect2d(len(self.map), len(self.map[0]))

        max_radius = grille_size.x
        radius = 1
        speed_cell = None
        cell_score = 0

        while speed_cell is None and radius < max_radius:
            speed_cell, cell_score = self.searchDest(radius, map_size)
            radius += 1

        if speed_cell is None:
            speed_cell = Vect2d(0, 0)
        else:
            speed_cell = speed_cell - self.pos

        dist_target = float("inf")
        dist_hunter = float("inf")

        speed_target = None
        speed_hunter = None

        for i in range(len(self.creature_info)):
            enemy_pos, enemy_score = self.creature_info[i]

            dist = Vect2d.dist(self.pos, enemy_pos)

            if enemy_score >= self.score + self.BASE_SCORE:
                if dist < dist_hunter:
                    speed_hunter = enemy_pos - self.pos
                    dist_hunter = dist
            elif enemy_score + self.BASE_SCORE <= self.score:
                if dist < dist_target:
                    speed_target = enemy_pos - self.pos
                    dist_target = dist

        if speed_hunter is None:
            speed_hunter = Vect2d(0, 0)

        if speed_target is None:
            speed_target = Vect2d(0, 0)

        coeff_target = 1 - dist_target/map_size.length()
        coeff_target = abs(coeff_target**3)
        coeff_target = coeff_target if coeff_target < 1 else 0

        coeff_hunter = 1 - dist_hunter/map_size.length()
        coeff_hunter = abs(coeff_hunter**3)
        coeff_hunter = coeff_hunter if coeff_hunter < 1 else 0

        # coeff_target *= coeff_hunter

        bords = [Vect2d(self.pos.x, 0),
                 Vect2d(self.pos.x, 0)]


        dist_bord = min(0, 0)


        self.speed = self.speed * 0.97
        self.speed += speed_cell*(1-coeff_target)*(1-coeff_hunter)
        self.speed += speed_target*coeff_target*(1-coeff_hunter)
        self.speed -= speed_hunter*(1-coeff_target)*coeff_hunter

        direction = self.speed.normalize()

        self.applyNewDirection(direction, map_size)
