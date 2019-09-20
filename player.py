import pygame

yellow = (255, 255, 0  )

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 10
        self.vx = 0
        self.vy = 0
        self.weight = 0

    def update(self, mx, my):
        coeff = 100

        dist_x = mx - self.x
        dist_y = my - self.y

        self.x += dist_x / coeff
        self.y += dist_y / coeff
        
    def display(self, window):
        pygame.draw.circle(window, yellow, (int(self.x), int(self.y)), self.radius)
