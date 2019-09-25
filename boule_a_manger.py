from color import Color
from display import Display

class Boule_a_manger:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = Color.couleurAleatoire()

    def display(self):
        Display.drawCircle(self.x,self.y,self.color,5)
