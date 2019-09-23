from color import Color
from display import Display

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.radius = 20

        self.weight = 0

    def update(self, mx, my):
        coeff = 100

        dist_x = mx - self.x
        dist_y = my - self.y

        self.x += dist_x / coeff
        self.y += dist_y / coeff

    def display(self):
        Display.drawCircle(x=self.x, y=self.y, color=Color.pink, radius=self.radius)
