import time
import random

from cell import Cell
from vector import Vect2d

class Map:
    @classmethod
    def init(cls, width:int, height:int, framerate:int) -> None:
        cls.width = width
        cls.height = height
        cls.all_cells = []

        cls.frame_time = 1/framerate

        cls.delta_t_new_cell = 0.2
        cls.ref_time = -1*cls.delta_t_new_cell

        cls.max_cells = 100

    @classmethod
    def createNewCell(cls) -> None:
        if time.time() - cls.ref_time > cls.delta_t_new_cell:
            cls.ref_time = time.time()

            x = random.randrange(0, cls.width)
            y = random.randrange(0, cls.height)
            cell = Cell(Vect2d(x, y))

            if len(cls.all_cells) <= cls.max_cells:
                cls.all_cells.append(cell)
            else :
                cls.all_cells.append(cell)
                del cls.all_cells[0]

    @classmethod
    def displayCell(cls) -> None:
        for i in range(0,len(cls.all_cells)):
            cls.all_cells[i].display()

    @classmethod
    def detectCellHitbox(cls, player:"Player") -> None:
        """

        INPUT :

        OUTPUT :
            None
        """

        for i in range(len(cls.all_cells)-1, -1, -1):
            cell_i = cls.all_cells[i]

            if Vect2d.distSq(player.pos, cell_i.pos) < (player.radius+cell_i.radius)**2:
                del cls.all_cells[i]
                player.score += 1
