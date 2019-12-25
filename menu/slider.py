from view.display import Display

from util.vector import Vect2d

from menu.widget import Widget

import math

class Slider(Widget):
    def __init__(self, pos, size, text, value, min_value, max_value, var):
        super().__init__(pos, size, text)

        self.value = value
        self.min_value = min_value
        self.max_value = max_value

        self.var = var

    def display(self, mouse_pos):
        """ Combination of static and dynamic graphics in a copy of
        the basic slide surface
        """

        Display.drawText(self.text, self.pos+self.size/2, 16, (255, 0, 0))

        return False

    def on_click(self, mouse_pos):
        """
        The dynamic part; reacts to movement of the slider button.
        """

        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini

        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi

"""
pygame.init()

font = pygame.font.SysFont("Verdana", 12)
screen = pygame.display.set_mode((2560, 1440), pygame.FULLSCREEN)
clock = pygame.time.Clock()

n = 4

coeff = Slider("Coeff", (4/3)*math.tan(math.pi/(2*n)), 2, -2, 150, 800)

add = []

for i in range(4):
    ligne = []

    for j in range(8):
        ligne.append(Slider("add_"+str(i)+str(j), 0, 2, -2, 150*(j+1), 1000+i*100))

    add.append(ligne)

slides = [[coeff]] + add

center = (300, 300)
radius = 100

steps = 50

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in range(len(slides)):
                for s in slides[i]:
                    if s.button_rect.collidepoint(pos):
                        s.hit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(slides)):
                for s in slides[i]:
                    s.hit = False
            if s.hit:
                s.move()
            s.draw()
"""
