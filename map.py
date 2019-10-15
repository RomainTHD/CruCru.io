import time
import random

from cell import Cell
from vector import Vect2d
from display import Display
from color import Color

from player import Player
from enemy import Enemy
from creature import Creature

class Map:
    @classmethod
    def init(cls, width:int, height:int, framerate:int) -> None:
        cls.width = width
        cls.height = height
        cls.all_cells = []

        cls.delta_t_new_cell = 0.2
        cls.ref_time = -1*cls.delta_t_new_cell

        cls.MAX_CELLS = 100

        cls.grille_width = 10
        cls.grille_height = 10

        cls.grille = [[[] for y in range(cls.grille_height)] for x in range(cls.grille_width)]

        cls.player = Player(Vect2d(cls.width/2, cls.height/2))
        # Création du joueur

        cls.enemies = []

        for i in range(1):
            v = Vect2d(random.randrange(Creature.base_radius, cls.width -Creature.base_radius), \
                       random.randrange(Creature.base_radius, cls.height-Creature.base_radius))

            cls.enemies.append(Enemy(v, "Ennemi "+str(i), Color.randomColor()))

    @classmethod
    def update(cls):
        cls.player.update(cls.width, cls.height)

        for i in range(len(cls.enemies)):
            pos_x, pos_y = cls.enemies[i].getMapPos(cls.width, cls.height, cls.grille_width, cls.grille_height)
            cls.enemies[i].map = cls.getLenSubMap(pos_x, pos_y)
            cls.enemies[i].update(cls.width, cls.height)

        for i in range(len(cls.enemies)):
            cls.detectCellHitbox(cls.enemies[i])

        cls.detectCellHitbox(cls.player)
        cls.createNewCell()

    @classmethod
    def getLenSubMap(cls, pos_x, pos_y):
        res = [[None for i in range(cls.grille_height)] for j in range(cls.grille_width)]

        for x in range(pos_x-cls.grille_width, pos_x+cls.grille_width+1):
            for y in range(pos_y-cls.grille_height, pos_y+cls.grille_height+1):
                if x >= 0 and x < cls.grille_width and y >= 0 and y < cls.grille_height:
                    res[x][y] = cls.grille[x][y]
                    
        return res

    @classmethod
    def createNewCell(cls) -> None:
        if time.time() - cls.ref_time > cls.delta_t_new_cell:
            cls.ref_time = time.time()

            x = random.randrange(0, cls.width)
            y = random.randrange(0, cls.height)
            cell = Cell(Vect2d(x, y))

            x = int(cell.pos.x / cls.width  * cls.grille_width )
            y = int(cell.pos.y / cls.height * cls.grille_height)

            cls.all_cells.append(cell)
            cls.grille[x][y].append(cell)

            if len(cls.all_cells) >= cls.MAX_CELLS:
                cls.deleteCell(0)

    @classmethod
    def display(cls):
        cls.displayCell()

        w = cls.width
        h = cls.height

        Display.drawLine(Vect2d(0, 0), Vect2d(w, 0))
        Display.drawLine(Vect2d(w, 0), Vect2d(w, h))
        Display.drawLine(Vect2d(w, h), Vect2d(0, h))
        Display.drawLine(Vect2d(0, h), Vect2d(0, 0))

        for x in range(cls.grille_width):
            for y in range(cls.grille_height):
                Display.drawText(len(cls.grille[x][y]), Vect2d((x+0.5)*cls.width/cls.grille_width, (y+0.5)*cls.height/cls.grille_height))

        for i in range(len(cls.enemies)):
            cls.enemies[i].display()

        cls.player.display()

    @classmethod
    def displayCell(cls) -> None:
        for i in range(0,len(cls.all_cells)):
            cls.all_cells[i].display()

    @classmethod
    def detectCellHitbox(cls, creature:"Creature") -> None:
        """

        INPUT :

        OUTPUT :
            None
        """

        for i in range(len(cls.all_cells)-1, -1, -1):
            cell_i = cls.all_cells[i]

            if Vect2d.distSq(creature.pos, cell_i.pos) < (creature.radius+cell_i.radius)**2:
                cls.deleteCell(i)
                creature.score += 1

    @classmethod
    def deleteCell(cls, index:int):
        cell = cls.all_cells[index]

        x = int(cell.pos.x / cls.width  * cls.grille_width )
        y = int(cell.pos.y / cls.height * cls.grille_height)

        for i in range(len(cls.grille[x][y])-1, -1, -1):
            if cell == cls.grille[x][y][i]:
                del cls.grille[x][y][i]

        del cls.all_cells[index]
