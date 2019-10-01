from color import Color
from display import Display
from map import Map

class Player:
    def __init__(self) -> None:
        self.x = Map.width/2
        self.y = Map.height/2

        self.base_radius = 20
        self.radius = self.base_radius

        self.score = 0

        self.name = "Player"

    def update(self, mx:int, my:int) -> None:
        coeff = 100

        dist_x = (mx - self.x)/coeff
        dist_y = (my - self.y)/coeff

        if self.x+dist_x > self.radius and self.x+dist_x < Map.width-self.radius:
            self.x += dist_x

        if self.y+dist_y > self.radius and self.y+dist_y < Map.height-self.radius:
            self.y += dist_y

        self.radius = int(self.base_radius + self.score/10)

    def update2(self, mx:int, my:int) -> None:
        coeff = 10

        dx = (mx - self.x)*coeff
        dy = (my - self.y)*coeff

        max_speed = 10

        speed = (dx**2 + dy**2)**0.5

        vx = dx/speed*coeff
        vy = dy/speed*coeff

        print(vx, vy)

        if self.x+vx > self.radius and self.x+vx < Map.width-self.radius:
            self.x += vx

        if self.y+vy > self.radius and self.y+vy < Map.height-self.radius:
            self.y += vy

        self.radius = int(self.base_radius + self.score/10)

    def display(self) -> None:
        Display.drawCircle(x=self.x, y=self.y, color=Color.PINK, radius=self.radius)
        Display.drawText(str(self.score), self.x, self.y, Color.WHITE)
