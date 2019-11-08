import random

if __name__ == "__main__":
    raise RuntimeError("Ne peut pas être lancé seul")

from util.vector import Vect2d
from util.color import Color

from view.camera import Camera
from view.display import Display
from view.skins import Skins

class Creature:
    BASE_RADIUS = 20
    BASE_SCORE = 1

    def __init__(self, pos: Vect2d, name: str, color: Color, id: int):
        self.pos = pos.copy()

        self.radius = self.BASE_RADIUS

        self.score = Creature.BASE_SCORE

        self.name = name

        self.color = color

        self.id = id

        self.is_alive = True

        self.img = Skins.getRandomSkin()

    def getMapPos(self, size, grille_size):
        pos_x = int(self.pos.x/size.x * grille_size.x)
        pos_y = int(self.pos.y/size.y * grille_size.y)

        return Vect2d(pos_x, pos_y)

    def update(self, size):
        pass

    def display(self) -> None:
        """
        Display.drawImg(img=self.img,
                        pos=self.pos,
                        radius=self.radius,
                        base_pos=Camera.pos)
        """

        Display.drawCircle(pos=self.pos, color=self.color, radius=self.radius, base_pos=Camera.pos)

        Display.drawText(text=self.score,
                         pos=self.pos,
                         base_pos=Camera.pos)

    def applyNewDirection(self, direction, size):
        coeff_tps = 1
        dist_per_sec = 200

        direction = direction*Display.frametime*dist_per_sec/coeff_tps

        direction *= ( 1/(self.score-self.BASE_SCORE+1) )**0.2

        new_pos = self.pos + direction

        if new_pos.x > self.radius and new_pos.x < size.x-self.radius:
            self.pos.x = new_pos.x

        if new_pos.y > self.radius and new_pos.y < size.y-self.radius:
            self.pos.y = new_pos.y

        while self.pos.x < self.radius:
            self.pos.x += 1

        while self.pos.x > size.x-self.radius:
            self.pos.x -= 1

        while self.pos.y < self.radius:
            self.pos.y += 1

        while self.pos.y > size.y-self.radius:
            self.pos.y -= 1

        self.radius = round(self.BASE_RADIUS + self.score/2)

    def kill(self, score):
        self.score += score

    def killed(self):
        self.is_alive = False

    def split(self):
        pass
