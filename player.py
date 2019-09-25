from color import Color
from display import Display
from map import Map

class Player:
    def __init__(self):
        self.x = Map.width/2
        self.y = Map.height/2

        self.base_radius = 20
        self.radius = self.base_radius

        self.score = 0

        self.name = "Player"

    def update(self, mx, my):
        coeff = 100

        dist_x = (mx - self.x)/coeff
        dist_y = (my - self.y)/coeff

        if self.x+dist_x > self.radius and self.x+dist_x < Map.width-self.radius:
            self.x += dist_x

        if self.y+dist_y > self.radius and self.y+dist_y < Map.height-self.radius:
            self.y += dist_y

        self.radius = int(self.base_radius + self.score/10)

    def display(self):
        Display.drawCircle(x=self.x, y=self.y, color=Color.pink, radius=self.radius)
        Display.drawText(str(self.score), self.x, self.y, Color.white)
