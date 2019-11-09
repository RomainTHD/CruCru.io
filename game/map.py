"""Terrain de jeu"""

import time
import random

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from view.display import Display
from view.camera import Camera

from util.vector import Vect2d
from util.color import Color

from entity.cell import Cell
from entity.player import Player
from entity.enemy import Enemy
from entity.creature import Creature

import config

class Map:
    """Terrain de jeu

    Attributs:
        size
        all_cells
        DELTA_T_NEW_CELL
        ref_time
        MAX_CELLS
        NB_CELL_PER_SECOND
        grille_size
        grille
        player
        enemies
        ENEMIES_MAX_SIZE
    """

    @classmethod
    def init(cls, width: int, height: int) -> None:
        """Initialisation de la map

        Args:
            width (int): largeur de la map
            height (int): hauteur de la map
        """

        cls.size = Vect2d(width, height)

        cls.MAX_CELLS = config.MAX_CELLS
        cls.NB_CELL_PER_SECOND = config.NB_CELL_PER_SECOND
        cls.DELTA_T_NEW_CELL = config.DELTA_T_NEW_CELL

        cls.grille_size = Vect2d(10, 10)

        cls.CREATURES_MAX_SIZE = config.MAX_CREATURES

        try:
            f = open("./data/usernames.txt", 'r')
        except FileNotFoundError:
            print("Pas de fichier usernames.txt")
            cls.all_usernames = None
        else:
            cls.all_usernames = []

            line = f.readline()

            while line != "":
                line = line.replace('\n', '')
                line = line.replace('\r', '')

                cls.all_usernames.append(line)
                line = f.readline()

            f.close()

        cls.reset()

    @classmethod
    def reset(cls):
        cls.ref_time = -1*cls.DELTA_T_NEW_CELL

        cls.all_cells = []

        cls.ref_time = -1*cls.DELTA_T_NEW_CELL

        cls.grille = [[[] for y in range(cls.grille_size.y)] for x in range(cls.grille_size.x)]

        cls.player_id = cls.generateId()

        cls.creatures = {}
        cls.creatures[cls.player_id] = [Player(Vect2d(cls.size.x/2, cls.size.y/2),
                                               "Player",
                                               Color.randomColor(),
                                               cls.player_id)
                                       ]
        # Création du joueur

    @classmethod
    def generateId(cls):
        return random.randrange(10**64)

    @classmethod
    def createEnemy(cls):
        ok = False
        timed_out = False
        compt = 0

        while not ok and not timed_out:
            ok = True

            pos = Vect2d(random.randrange(Creature.BASE_RADIUS*2, cls.size.x-Creature.BASE_RADIUS*2),
                         random.randrange(Creature.BASE_RADIUS*2, cls.size.y-Creature.BASE_RADIUS*2))

            for k in cls.creatures.keys():
                creatures_list = cls.creatures[k]

                for creature in creatures_list:
                    if Vect2d.dist(pos, creature.pos) < (Creature.BASE_RADIUS + creature.radius)*2:
                        ok = False

            if compt == 5:
                timed_out = True

            compt += 1

        if not timed_out:
            enemy_id = cls.generateId()

            if cls.all_usernames is None:
                size = random.randint(3, 5)
                name = cls.generateNewName(size)
            else:
                name = cls.all_usernames[random.randrange(len(cls.all_usernames))]

            enemy = Enemy(pos, name, Color.randomColor(), enemy_id)

            cls.creatures[enemy_id] = [enemy]

    @staticmethod
    def generateNewName(size: int):
        consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')
        vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'ai', 'ei', 'eu', 'ey', 'ie', 'io', 'oi', 'ou', 'oy', 'ya', 'ye', 'yi', 'yo', 'yu')

        name = ""

        for i in range(size):
            name += consonants[random.randrange(len(consonants))]
            name += vowels[random.randrange(len(vowels))]

        return name

    @classmethod
    def setMousePos(cls, mouse_pos: Vect2d):
        for player in cls.creatures[cls.player_id]:
            player.mouse_pos = mouse_pos - Vect2d(Display.size.x/2, Display.size.y/2)

    @classmethod
    def update(cls):
        if len(cls.creatures) < cls.CREATURES_MAX_SIZE:
            cls.createEnemy()

        for player in cls.creatures[cls.player_id]:
            player.update(cls.size)

        creatures_info = []

        for k in cls.creatures.keys():
            creatures_list = cls.creatures[k]

            for creature in creatures_list:
                creatures_info.append((creature.pos.copy(), creature.radius, creature.score))

        for k in cls.creatures.keys():
            enemy_list = cls.creatures[k]

            if k != cls.player_id:
                for enemy in enemy_list:
                    enemy.setMapCell(cls.getCellPosMap())
                    enemy.setCreaturesInfo(creatures_info)
                    enemy.update(cls.size)

        for k in cls.creatures.keys():
            creatures_list = cls.creatures[k]

            for creature in creatures_list:
                cls.detectCellHitbox(creature)

        cls.detectEnemyHitbox()

        for k in list(cls.creatures.keys()):
            for i in range(len(cls.creatures[k])-1, -1, -1):
                if not cls.creatures[k][i].is_alive:
                    del cls.creatures[k][i]

            if len(cls.creatures[k]) == 0:
                del cls.creatures[k]

        for i in range(cls.NB_CELL_PER_SECOND):
            cls.createNewCell()

    @classmethod
    def getPlayerPos(cls):
        pos = Vect2d(0, 0)

        if cls.isPlayerAlive():
            for player in cls.creatures[cls.player_id]:
                pos += player.pos

            pos /= len(cls.creatures[cls.player_id])

        return pos

    @classmethod
    def isPlayerAlive(cls):
        try:
            is_alive = cls.creatures[cls.player_id][0].is_alive
        except KeyError:
            is_alive = False

        return is_alive

    @classmethod
    def detectEnemyHitbox(cls):
        for k1 in cls.creatures.keys():
            for k2 in cls.creatures.keys():
                if k1 != k2:
                    enemy_list_1 = cls.creatures[k1]
                    enemy_list_2 = cls.creatures[k2]

                    for enemy_1 in enemy_list_1:
                        for enemy_2 in enemy_list_2:
                            if enemy_1.is_alive and enemy_2.is_alive:
                                dist = Vect2d.dist(enemy_1.pos, enemy_2.pos)

                                if dist <= max(enemy_1.radius, enemy_2.radius):
                                    if Creature.canEat(enemy_1.score, enemy_2.score):
                                        enemy_1.kill(enemy_2.score)
                                        enemy_2.killed()
                                    elif Creature.canEat(enemy_2.score, enemy_1.score):
                                        enemy_2.kill(enemy_1.score)
                                        enemy_1.killed()

    @classmethod
    def getCellPosMap(cls):
        res = [[None for i in range(cls.grille_size.y)] for j in range(cls.grille_size.x)]

        for x in range(cls.grille_size.x):
            for y in range(cls.grille_size.y):
                content = []

                for cell in cls.grille[x][y]:
                    content.append(cell.pos.copy())

                res[x][y] = tuple(content)
        return res

    @classmethod
    def createNewCell(cls) -> None:
        if time.time() - cls.ref_time > cls.DELTA_T_NEW_CELL:
            cls.ref_time = time.time()

            x = random.randrange(Cell.BASE_RADIUS, cls.size.x-Cell.BASE_RADIUS)
            y = random.randrange(Cell.BASE_RADIUS, cls.size.y-Cell.BASE_RADIUS)
            cell = Cell(Vect2d(x, y))

            ok = True

            for k in cls.creatures.keys():
                enemy_list = cls.creatures[k]

                for enemy in enemy_list:
                    if Vect2d.dist(enemy.pos, cell.pos) < cell.radius + enemy.radius:
                        ok = False

            x = int(cell.pos.x / cls.size.x * cls.grille_size.x)
            y = int(cell.pos.y / cls.size.y * cls.grille_size.y)

            if ok:
                cls.all_cells.append(cell)
                cls.grille[x][y].append(cell)

            if len(cls.all_cells) >= cls.MAX_CELLS:
                cls.deleteCell(0)

    @classmethod
    def display(cls):
        w = cls.size.x
        h = cls.size.y

        if config.DEBUG:
            for x in range(cls.grille_size.x):
                for y in range(cls.grille_size.y):
                    Display.drawText(len(cls.grille[x][y]),
                                     Vect2d((x+0.5)*cls.size.x/cls.grille_size.x, (y+0.5)*cls.size.y/cls.grille_size.y),
                                     base_pos=Camera.pos)

        for x in range(1, cls.grille_size.x):
            Display.drawLine(Vect2d(x*w/cls.grille_size.x, 0),
                             Vect2d(x*w/cls.grille_size.x, h),
                             color=Color.DARK_GRAY,
                             base_pos=Camera.pos)

        for y in range(1, cls.grille_size.y):
            Display.drawLine(Vect2d(0, y*h/cls.grille_size.y),
                             Vect2d(w, y*h/cls.grille_size.y),
                             color=Color.DARK_GRAY,
                             base_pos=Camera.pos)

        Display.drawLine(Vect2d(0, 0), Vect2d(w, 0), color=Color.RED, base_pos=Camera.pos)
        Display.drawLine(Vect2d(w, 0), Vect2d(w, h), color=Color.RED, base_pos=Camera.pos)
        Display.drawLine(Vect2d(w, h), Vect2d(0, h), color=Color.RED, base_pos=Camera.pos)
        Display.drawLine(Vect2d(0, h), Vect2d(0, 0), color=Color.RED, base_pos=Camera.pos)

        cls.displayCell()

        for k in cls.creatures.keys():
            enemy_list = cls.creatures[k]

            if k != cls.player_id:
                for enemy in enemy_list:
                    enemy.display()

        if cls.isPlayerAlive():
            for player in cls.creatures[cls.player_id]:
                player.display()

    @classmethod
    def displayCell(cls) -> None:
        for i in range(len(cls.all_cells)):
            cls.all_cells[i].display()

    @classmethod
    def splitCreature(cls, creature):
        if creature.score > creature.BASE_SCORE*3:
            creature.split()

    @classmethod
    def splitPlayer(cls):
        pass

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
                creature.score += cell_i.score
                cls.deleteCell(i)

    @classmethod
    def deleteCell(cls, index:int):
        cell = cls.all_cells[index]

        x = int(cell.pos.x/cls.size.x * cls.grille_size.x)
        y = int(cell.pos.y/cls.size.y * cls.grille_size.y)

        for i in range(len(cls.grille[x][y])-1, -1, -1):
            if cell == cls.grille[x][y][i]:
                del cls.grille[x][y][i]

        del cls.all_cells[index]
