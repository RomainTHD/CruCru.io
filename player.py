from color import Color
from display import Display
from map import Map
from vector import Vect2d
from camera import Camera

class Player:
    def __init__(self) -> None:
        self.pos = Vect2d(Map.width/2, Map.height/2)

        self.base_radius = 20
        self.radius = self.base_radius

        self.score = 0

        self.name = "Player"

    def update2(self, mx:int, my:int) -> None:
        coeff = 100

        dist_x = (mx - self.x)/coeff
        dist_y = (my - self.y)/coeff

        if self.x+dist_x > self.radius and self.x+dist_x < Map.width-self.radius:
            self.x += dist_x

        if self.y+dist_y > self.radius and self.y+dist_y < Map.height-self.radius:
            self.y += dist_y

        self.radius = int(self.base_radius + self.score/10)

    def update(self, v:Vect2d) -> None:
        coeff_tps = 1
        dist_per_sec = 200

        if v.lengthSq() > self.radius**2:
            coeff_dist_mouse = 1
        else:
            coeff_dist_mouse = v.length()/self.radius

        v = v.normalize()

        v = v*Map.frame_time*dist_per_sec/coeff_tps * coeff_dist_mouse**2

        max_speed_per_s = 100

        new_pos = self.pos + v

        if new_pos.x > self.radius and new_pos.x < Map.width-self.radius:
            self.pos.x = new_pos.x

        if new_pos.y > self.radius and new_pos.y < Map.height-self.radius:
            self.pos.y = new_pos.y

        self.radius = int(self.base_radius + self.score/10)

    def display(self) -> None:
        Display.drawCircle(pos=self.pos, color=Color.PINK, radius=self.radius)
        Display.drawText(text_str=str(self.score), pos=self.pos, color=Color.WHITE)
