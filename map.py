import time
import random

from boule_a_manger import Boule_a_manger

class Map:
    @classmethod
    def init(cls, width, height):
        cls.width = width
        cls.height = height
        cls.liste_boules=[]

        cls.delta_t = 0.2
        cls.ref_time = -1*cls.delta_t

        cls.max_cells = 100

    @classmethod
    def creer_boule(cls):
        if time.time() - cls.ref_time > cls.delta_t:
            cls.ref_time = time.time()

            x = random.randrange(0, cls.width)
            y = random.randrange(0,cls.height)
            b = Boule_a_manger(x,y)

            if len(cls.liste_boules) <= cls.max_cells:
                cls.liste_boules += [b]
            else :
                del cls.liste_boules[0]
                cls.liste_boules += [b]

    @classmethod
    def affiche_cellule(cls):
        for i in range(0,len(cls.liste_boules)):
            cls.liste_boules[i].display()

    @classmethod
    def hitbox_cellule(cls, player):
        for i in range(len(cls.liste_boules)-1, -1, -1):
            if (player.x-cls.liste_boules[i].x)**2 + (player.y-cls.liste_boules[i].y)**2 < (player.radius+cls.liste_boules[i].radius)**2:
                del cls.liste_boules[i]
                player.score += 1
