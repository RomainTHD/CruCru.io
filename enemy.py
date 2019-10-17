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

        # self.angle = random.random()*math.pi*2

        self.dest_coords = Vect2d((random.random()-0.5)*1000, (random.random()-0.5)*1000)
        self.dest_score = -1

    def getMapPos(self, width, height, grille_width, grille_height):
        pos_x = int(self.pos.x/width  * grille_width)
        pos_y = int(self.pos.y/height * grille_height)

        return pos_x, pos_y

    def update(self, width, height):
        maxi = 0
        liste_pos_maxi = []

        grille_width  = len(self.map)
        grille_height = len(self.map[0])

        pos_x, pos_y = self.getMapPos(width, height, grille_width, grille_height)

        radius = 1

        for x in range(pos_x-radius, pos_x+radius+1):
            for y in range(pos_y-radius, pos_y+radius+1):
                if x in range(grille_width) and y in range(grille_height):
                    taille = len(self.map[x][y])

                    if taille == maxi:
                        liste_pos_maxi += [(x, y)]
                    elif taille > maxi:
                        maxi = taille
                        liste_pos_maxi = [(x, y)]



        if maxi > self.dest_score:
            self.dest_score = maxi

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

            if coords_mini is not None:
                self.dest_coords = coords_mini.copy()







        v = self.dest_coords.copy()
















        coeff_tps = 1
        dist_per_sec = 100

        v = v.normalize()
        v = v*Display.frame_time*dist_per_sec/coeff_tps

        max_speed_per_s = 100

        new_pos = self.pos + v

        if new_pos.x > self.radius and new_pos.x < width-self.radius:
            self.pos.x = new_pos.x

        if new_pos.y > self.radius and new_pos.y < height-self.radius:
            self.pos.y = new_pos.y

        self.radius = int(self.base_radius + self.score/10)
