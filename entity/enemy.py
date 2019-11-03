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

    def __init__(self, pos, name, color) -> None:
        super().__init__(pos, name, color)

        self.map = None
        self.creature_info = None

        self.speed = Vect2d(random.random()*2-1, random.random()*2-1)

    def searchDest(self, radius, size):
        maxi = 0
        liste_pos_maxi = []

        score = 0

        grille_size = Vect2d(len(self.map), len(self.map[0]))

        map_pos = self.getMapPos(size, grille_size)

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

    def update(self, size):
        dest = None
        best_score = 0
        radius = 1

        grille_size = Vect2d(len(self.map), len(self.map[0]))

        max_radius = grille_size.x

        while dest is None and radius < max_radius:
            dest, best_score = self.searchDest(radius, size)
            radius += 1

        v = self.getMapPos(size, grille_size)
        radius = 3
        bord = 2

        dist_cible = float("inf")
        dist_chasseur = float("inf")

        pos_cible = None
        pos_chasseur = None

        for i in range(len(self.creature_info)):
            enemy_pos, enemy_score = self.creature_info[i]

            if enemy_score > self.score:
                if Vect2d.dist(self.pos, enemy_pos) < dist_chasseur:
                    pos_chasseur = enemy_pos
            else:
                if Vect2d.dist(self.pos, enemy_pos) < dist_cible:
                    pos_cible = enemy_pos

        if dest is not None:
            self.speed = dest - self.pos + self.speed*0.98

        direction = self.speed.normalize()

        self.applyNewDirection(direction, size)
