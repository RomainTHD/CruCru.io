from random import randrange
from boule_a_manger import Boule_a_manger

class Map:
    @classmethod
    def init(cls, width, height):
        cls.width = width
        cls.height = height
        cls.liste_boules=[]

    @classmethod
    def creer_boule(cls):
        for i in range(0,5):
            x = randrange(0, cls.width)
            y = randrange(0,cls.height)
            b = Boule_a_manger(x,y)
            if len(cls.liste_boules)<=100 : 
                cls.liste_boules += [b]
            else :
                del cls.liste_boules[0:3]
                cls.liste_boules += [b]
        
    @classmethod
    def affiche_cellule(cls)
        for i in range(0,len(liste_boules)):
            liste_boules[i].display()
                
    
    
