"""Gestion et chargement des skins"""

import os
# Utilisé pour parcourir les fichiers

import random
# Pour obtenir un skin random

import pygame
import pygame.gfxdraw
# Pour le chargement des skins

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.color import Color
# Pour la couleur des pixels

from util.vector import Vect2d
# Pour les positions

import config
# Pour connaitre la valeur de DEBUG

class Skins:
    """Classe s'occupant des skins

    Attributs:
        PATH (str): chemin, vaut "./data" ou "../data"
        all_skins (dict of pygame.Surface and str): dictionnaire ayant en clé les noms des skins
                                                    et en valeurs l'image (pygame.Surface) et la
                                                    description de ce skin
    """

    PATH = "./data"

    @classmethod
    def init(cls):
        """Initialisation, chargement des images"""

        if config.DEBUG:
            print("Loading skins...")

        cls.all_skins = {}

        all_img = cls.loadAll() # On charge les images

        compt = 0

        for name in all_img.keys():
            img, desc = all_img[name]

            circle = cls.imgToCircle(img)
            # On transforme l'image (carrée) en cercle avec de la transparence

            cls.all_skins[name] = (circle, desc)

            compt += 1

            if config.DEBUG:
                print("{0}/{1}".format(compt, len(all_img.values())))

        if config.DEBUG:
            print("Skins loaded")

    @classmethod
    def loadAll(cls):
        """Charge toutes les images carrées

        Returns:
            all_img (dict of pygame.Surface and str): dictionnaire ayant en clé les noms des skins
                                                      et en valeurs l'image et la description
        """

        all_img = {}

        all_file_name_full = os.listdir(cls.PATH + "/skins")
        # Liste du contenu du dossier data/skins

        for file_name_full in all_file_name_full:
            file_name = file_name_full.split('.')
            extension = file_name[-1]
            del file_name[-1]
            file_name = ''.join(file_name)

            # On récupère le nom et l'extension de chaque fichier

            try:
                f = open(cls.PATH + "/description/" + file_name + ".txt", 'r')
            except FileNotFoundError:
                desc = "Pas de description"
            else:
                desc = f.read()
                f.close()

            # On récupère la description du fichier

            if extension in ("png", "jpg"):
                img = pygame.image.load(cls.PATH + "/skins/" + file_name + '.' +extension).convert()
                all_img[file_name] = (img, desc)

                # On charge l'image

        return all_img

    @classmethod
    def imgToCircle(cls, img: pygame.Surface):
        """Méthode transformant l'image de base afin de la rendre ronde
        et d'ajouter la transparence
        """

        width = img.get_width()
        height = img.get_height()

        if width == height:
            size = width
        else:
            msg = "L'image n'est pas un carré. Dimensions: ({0},{1})".format(width, height)
            raise ValueError(msg)

        # Vérification des dimensions

        circle_surface = pygame.Surface((size+1, size+1), pygame.SRCALPHA)
        # On crée le cercle

        center = Vect2d(size/2, size/2)
        radius = int(size/2)

        for x in range(size):
            for y in range(size):
                pos = Vect2d(x, y)

                if Vect2d.distSq(pos, center) < radius**2:
                    color = img.get_at((x, y))

                    # Si le pixel est dans le cercle de destination on prend sa couleur

                    if color[3] != 255:
                        color[3] = 255
                        # On supprime la transparence

                    if color == Color.TO_TRANSPARENT:
                        # Cette couleur est une valeur spéciale qui sera remplacée par de la
                        # transparence à l'écran, il ne faut donc pas que l'image originale en
                        # contienne

                        print("L'image contient des pixels transparents")

                        color[0] += 1
                else:
                    color = Color.TRANSPARENT
                    # Si l'on est hors du cercle on prend comme couleur transparent

                pygame.gfxdraw.pixel(circle_surface, x, y, color)
                # On dessine le pixel

        pygame.gfxdraw.aacircle(circle_surface, int(size/2), int(size/2), radius, Color.RED)
        # On dessine un cercle ayant de l'anti-aliasing pour délimiter la bordure du skin

        circle_surface.set_colorkey(Color.TO_TRANSPARENT)
        # On supprime la couleur indésirable
        # NOTE: même si ce rendu est plus rapide que l'affichage d'un pixel transparent et donc
        # préférable, il est incompatible avec l'anti-aliasing. Par soucis d'esthetique on
        # privilégiera donc ici l'affichage de pixels transparents

        circle_surface = circle_surface.convert_alpha()
        # On précise que cette image accepte la transparence

        return circle_surface

    @classmethod
    def getRandomSkin(cls):
        """Retourne un skin aléatoire parmi ceux chargés

        Returns
            skin (pygame.Surface): skin aléatoire
        """

        keys = list(cls.all_skins.keys())

        n = random.randrange(len(keys))
        k = keys[n]

        skin, desc = cls.all_skins[k]

        return skin

if __name__ == "__main__":
    # Petite vérification de tous les skins importés

    import random

    Skins.PATH = "../data"

    pygame.init()
    window = pygame.display.set_mode((1000, 1000), pygame.SRCALPHA)

    Skins.init()

    pygame.draw.rect(window, (200, 200, 255), (0, 0, 1000, 1000))

    all_img = []

    for key in Skins.all_skins.keys():
        img, desc = Skins.all_skins[key]

        all_img.append(img)

    clock = pygame.time.Clock()

    finished = False
    framecount = 0

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                finished = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    finished = True

        pygame.draw.rect(window, (200, 200, 255), (0, 0, 1000, 1000))

        window.blit(all_img[(framecount//60)%len(all_img)], (100, 100))

        pygame.display.update()

        clock.tick(60)

        framecount += 1
