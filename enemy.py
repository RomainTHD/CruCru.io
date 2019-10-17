from display import Display
from vector import Vect2d
from creature import Creature
from cell import Cell

import math
import random

class Enemy(Creature):
    def __init__(self, pos, name, color) -> None:
        super().__init__(pos, name, color)

        self.map = None

        self.speed = Vect2d()

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
                cell = self.map[x][y][j]

                dist = Vect2d.dist(cell.pos, self.pos)

                if dist < distance_mini:
                    distance_mini = dist
                    coords_mini = self.map[x][y][j].pos

        return coords_mini

    def update(self, width, height):
        coords_mini = None
        radius = 1

        while coords_mini is None and radius < 100:
            coords_mini = self.searchDest(radius, width, height)
            radius += 1

        if coords_mini is None:
            coords_mini = Vect2d()

        dest = coords_mini.copy()

        self.speed = dest - self.pos + self.speed*0.98

        direction = self.speed.normalize()

        self.applyNewDirection(direction, width, height)
