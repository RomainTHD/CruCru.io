if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.vector import Vect2d
from util.color import Color

from view.display import Display

class Creature:
    base_radius = 20

    def __init__(self, pos:Vect2d, name:str, color:Color=Color.PINK):
        self.pos = pos.copy()

        self.radius = self.base_radius

        self.score = 5

        self.name = name

        self.color = color

        self.is_alive = True

    def getMapPos(self, width, height, grille_width, grille_height):
        pos_x = int(self.pos.x/width  * grille_width)
        pos_y = int(self.pos.y/height * grille_height)

        return Vect2d(pos_x, pos_y)

    def update(self, width, height):
        pass

    def display(self) -> None:
        Display.drawCircle(pos=self.pos, color=self.color, radius=self.radius)
        Display.drawText(text_str=str(self.score), pos=self.pos, color=Color.WHITE)

    def applyNewDirection(self, direction, width, height):
        coeff_tps = 1
        dist_per_sec = 100

        direction = direction*Display.frame_time*dist_per_sec/coeff_tps

        new_pos = self.pos + direction

        if new_pos.x > self.radius and new_pos.x < width-self.radius:
            self.pos.x = new_pos.x

        if new_pos.y > self.radius and new_pos.y < height-self.radius:
            self.pos.y = new_pos.y

        self.radius = int(self.base_radius + self.score/10)
