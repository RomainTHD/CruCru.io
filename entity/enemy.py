from util.vector import Vect2d

from entity.creature import Creature

import math
import random

class Enemy(Creature):
    def __init__(self, pos, name, color) -> None:
        super().__init__(pos, name, color)

        self.map = None

        self.speed = Vect2d(random.random()*2-1, random.random()*2-1)

    def searchDest(self, radius, width, height):
        maxi = 0
        liste_pos_maxi = []

        grille_width  = len(self.map)
        grille_height = len(self.map[0])

        map_pos = self.getMapPos(width, height, grille_width, grille_height)

        for x in range(map_pos.x-radius, map_pos.x+radius+1):
            for y in range(map_pos.y-radius, map_pos.y+radius+1):
                if x in range(grille_width) and y in range(grille_height):
                    taille = len(self.map[x][y])

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
                    distance_mini = dist
                    coords_mini = self.map[x][y][j]

        return coords_mini

    def update(self, width, height):
        dest = None
        radius = 1

        grille_width  = len(self.map)
        grille_height = len(self.map[0])

        max_radius = int(grille_width*20/100)

        while dest is None and radius < max_radius:
            dest = self.searchDest(radius, width, height)
            radius += 1

        if dest is not None:
            self.speed = dest - self.pos + self.speed*0.98

        direction = self.speed.normalize()

        self.applyNewDirection(direction, width, height)
