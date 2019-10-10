from display import Display
from vector import Vect2d
from creature import Creature

import math
import random

class Enemy(Creature):
    def __init__(self, pos, name, color) -> None:
        super().__init__(pos, name, color)

        self.angle = random.random()*math.pi*2

    def update(self, width, height):
        v = Vect2d(math.cos(self.angle), math.sin(self.angle)) * 100

        self.angle += 0.05

        coeff_tps = 1
        dist_per_sec = 200

        if v.lengthSq() > self.radius**2:
            coeff_dist_mouse = 1
        else:
            coeff_dist_mouse = v.length()/self.radius

        v = v.normalize()

        v = v*Display.frame_time*dist_per_sec/coeff_tps * coeff_dist_mouse**2

        max_speed_per_s = 100

        new_pos = self.pos + v

        if new_pos.x > self.radius and new_pos.x < width-self.radius:
            self.pos.x = new_pos.x

        if new_pos.y > self.radius and new_pos.y < height-self.radius:
            self.pos.y = new_pos.y

        self.radius = int(self.base_radius + self.score/10)
