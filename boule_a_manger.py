from color import Color

class Boule_a_manger:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = Color.couleurAleatoire()
