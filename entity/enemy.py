if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.vector import Vect2d

from entity.creature import Creature

import math
import random

class Enemy(Creature):
    def __init__(self, pos, name, color) -> None:
        super().__init__(pos, name, color)

        self.map = None
        self.creature_map_info = None

        self.speed = Vect2d(random.random()*2-1, random.random()*2-1)

    def searchDest(self, radius, width, height):
        maxi = 0
        liste_pos_maxi = []

        score = 0

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
                    score = len(self.map[x][y])
                    distance_mini = dist
                    coords_mini = self.map[x][y][j]

        return coords_mini, score

    def update(self, width, height):
        dest = None
        best_score = 0
        radius = 1

        grille_width  = len(self.map)
        grille_height = len(self.map[0])

        max_radius = grille_width

        while dest is None and radius < max_radius:
            dest, best_score = self.searchDest(radius, width, height)
            radius += 1

        v = self.getMapPos(width, height, grille_width, grille_height)
        radius = 3
        bord = 2

        enemies_info = []

        for x in range(v.x-radius, v.x+radius+1):
            for y in range(v.y-radius, v.y+radius+1):
                if x in range(bord, grille_width-bord) and y in range(bord, grille_height-bord):
                    if len(self.creature_map_info[x][y]) != 0:
                        enemies_info += self.creature_map_info[x][y]

        for i in range(len(enemies_info)):
            enemy_pos, enemy_score = enemies_info[i] 
            
            if enemy_score < self.score:
                dest = enemy_pos
            else:
                dest = enemy_pos*-1

        if dest is not None:
            self.speed = dest - self.pos + self.speed*0.98

        direction = self.speed.normalize()

        self.applyNewDirection(direction, width, height)
