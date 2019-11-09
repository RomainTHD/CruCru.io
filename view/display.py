"""Affichage, gestion de la fenêtre, dessin à l'écran"""

import time

import pygame
import pygame.gfxdraw

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.color import Color
from util.vector import Vect2d

class Display:
    """Classe statique gérant l'affichage de la fenêtre

    Attributs:
        exec_when_resized (list of function): fonctions à exécuter lorsque la taille de la fenêtre
                                              est modifiée

        screen_size (Vect2d): taille de l'écran
        size (Vect2d): taille de la fenêtre
        windowed_size (Vect2d): taille de la fenêtre en mode fenêtré, pour garder la même taille à
                                la sortie du mode plein écran
        is_fullscreen (bool): si la fenêtre est en plein écran ou non

        framerate (int): nombre d'images par seconde
        framecount (int): nombre d'images écoulées
        frametime (float): temps d'une image

        clock (pygame.time.Clock): horloge interne

        all_font (dict of dict of pygame.font): dictionnaire ayant en clé le nom des polices puis
                                                en valeur un second dictionnaire ayant en clé la
                                                taille des polices et en valeur la police chargée.
                                                Ce dictionnaire est utile afin de ne charger qu'une
                                                seule fois chaque police

        window (pygame.Surface): fenêtre pygame
    """

    exec_when_resized: list = []

    screen_size: Vect2d

    windowed_size: Vect2d

    size: Vect2d
    is_fullscreen: bool = False

    framerate: int
    real_framerate: int
    framecount: int = 0
    frametime: float = time.time()
    frametimes: [int] = [0]*10

    clock: pygame.time.Clock

    all_font: dict = {}

    window: pygame.Surface = None

    def __new__(cls):
        """Méthode appelée lors d'une instanciation de la classe
        La classe étant statique, une exception sera levée

        Raises:
            RuntimeError: en cas d'instanciation
        """

        raise RuntimeError("Classe statique, instanciation impossible")

    @staticmethod
    def setCursorArrow():
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        # pygame.mouse.set_cursor(*pygame.cursors.tri_left)

    @staticmethod
    def setCursorHand():
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)

    @classmethod
    def init(cls, width: int, height: int, start_fullscreen: bool, framerate: int) -> None:
        """Initialisation de l'affichage

        Args:
            width (int): largeur de la fenêtre
            height (int): hauteur de la fenêtre
            start_fullscreen (bool): plein écran au démarrage ou non
            framerate (int): nombre d'images par seconde
        """

        cls.setCursorArrow()

        cls.screen_size = Vect2d(pygame.display.Info().current_w, pygame.display.Info().current_h)
        # Taille de l'écran

        cls.size = Vect2d(width, height)
        # Taille de la fenêtre

        cls.zoom_factor = 1

        cls.windowed_size = cls.size.copy()

        cls.framerate = framerate
        cls.real_framerate = cls.framerate

        cls.clock = pygame.time.Clock()

        PATH = "data/icon.png"

        try:
            f = open(PATH, 'r')
        except FileNotFoundError:
            print("Icône introuvable")
        else:
            f.close()

            icon = pygame.image.load(PATH)
            pygame.display.set_icon(icon)

        cls.resize(cls.size.x, cls.size.y)
        # Cette opération va aussi créer la fenêtre

        if start_fullscreen:
            cls.toggleFullscreen()

        cls.updateFrame()
        # On actualise la fenêtre

    @classmethod
    def updateTitle(cls):
        pygame.display.set_caption("Agar.io - " + str(cls.real_framerate) + " fps")
        # On change le titre

    @classmethod
    def toggleFullscreen(cls) -> None:
        """Procédure exécutée lorsque la touche F11 est enfoncée, pour le plein écran"""

        cls.is_fullscreen = not cls.is_fullscreen
        # On inverse la valeur de is_fullscreen

        if cls.is_fullscreen:
            cls.resize(cls.screen_size.x, cls.screen_size.y)
            # Si l'on est en plein écran on va mettre la taille de la fenêtre à la taille de l'écran
        else:
            cls.resize(cls.windowed_size.x, cls.windowed_size.y)
            # Sinon on va mettre la taille de la fenêtre à une certaine taille

    @classmethod
    def resize(cls, w: int, h: int) -> None:
        """Fonction pour changer la taille de la fenêtre
        Cette fonction va recréer la fenêtre

        Args:
            w (int): nouvelle largeur de la fenêtre
            h (int): nouvelle hauteur de la fenêtre
        """

        if cls.is_fullscreen:
            cls.window = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
        else:
            cls.window = pygame.display.set_mode((w, h), pygame.RESIZABLE)
            cls.windowed_size.x = w
            cls.windowed_size.y = h

        cls.size.x = w
        cls.size.y = h

        for f in cls.exec_when_resized:
            f(w, h)

    @classmethod
    def execWhenResized(cls, f: 'function') -> None:
        """Procédure permettant d'ajouter une fonction à la liste des fonctions à exécuter lors d'un
        changement de la taille de la fenêtre

        Args:
            f (function): fonction à exécuter
        """

        cls.exec_when_resized.append(f)
        # On ajoute la fonction

    @classmethod
    def updateFrame(cls, color: Color = Color.BLACK) -> None:
        """Procédure pour mettre à jour la fenêtre"""

        pygame.display.flip()
        # On met à jour l'écran

        if len(color) == 3:
            cls.window.fill(color)
            # On efface l'arrière-plan
        else:
            cls.drawRect(Vect2d(0, 0), cls.size, color)

        cls.updateTitle()

        del cls.frametimes[0]
        cls.frametimes.append(time.time() - cls.frametime)

        frametime = sum(cls.frametimes)/len(cls.frametimes)

        if frametime == 0:
            cls.real_framerate = float("inf")
        else:
            cls.real_framerate = round(1/frametime)

        cls.frametime = time.time()

        cls.clock.tick(cls.framerate)
        # Pour actualiser la fenêtre après un certain temps

        cls.framecount += 1

    @classmethod
    def screenshot(cls) -> pygame.Surface:
        return cls.window.copy()

    @classmethod
    def zoom(cls, zoom_factor: int):
        cls.zoom_factor = 1

    @classmethod
    def drawCircle(cls, pos: Vect2d, color: Color, radius: int, base_pos: Vect2d = Vect2d(0, 0), fill: bool = True) -> None:
        """Procédure pour dessiner un cercle à l'écran

        Args:
            pos (Vect2d): position du centre du cercle
            color (Color): couleur RGBA
            radius (int): rayon du cercle
            base_pos (Vect2d): position de référence de la fenêtre
            fill (bool): cercle rempli ou non
        """

        pos = pos.copy()

        if base_pos.length() != 0:
            pos = (pos - base_pos)*cls.zoom_factor

        pos = pos.toIntValues()

        radius = int(radius*cls.zoom_factor)

        if fill:
            pygame.gfxdraw.filled_circle(cls.window, pos.x, pos.y, radius, color)
            # Dessine un cercle plein

        pygame.gfxdraw.aacircle(cls.window, pos.x, pos.y, radius, color)
        # Dessine un cercle vide étant soumis à l'anti-aliasing (anticrénelage), ayant un rendu plus
        # lisse qu'un cercle normal

    @classmethod
    def drawRect(cls, pos: Vect2d, size: Vect2d, color: Color, base_pos: Vect2d = Vect2d(0, 0), fill: bool = True) -> None:
        """Procédure pour dessiner un rectangle à l'écran

        Args:
            pos (Vect2d): position du coin en haut à gauche rectangle
            size (Vect2d): taille du rectangle
            color (Color): couleur RGBA
            base_pos (Vect2d): position de référence de la fenêtre
            fill (bool): rectangle rempli ou non
        """

        size = size.copy()
        pos = pos.copy()

        if base_pos.length() != 0:
            pos = (pos - base_pos)*cls.zoom_factor

        pos = pos.toIntValues()

        if base_pos.length() != 0:
            size *= cls.zoom_factor

        size = size.toIntValues()

        rect = pygame.Rect(pos.toTuple(), size.toTuple())

        if fill:
            pygame.gfxdraw.box(cls.window, rect, color)
        else:
            pygame.gfxdraw.rectangle(cls.window, rect, color)

    @classmethod
    def drawText(cls, text: str, pos: Vect2d, size: int = 16, color: Color = Color.WHITE, base_pos: Vect2d = Vect2d(0, 0)) -> None:
        """Procédure pour afficher du texte à l'écran
        On essaie de garder en mémoire les polices chargées pour éviter de recharger la police à
        chaque frame

        Args:
            text (str): texte à afficher
            pos (Vect2d): position du texte
            size (int): taille de la police utilisée
            color (Color): couleur du texte, blanc par défaut
            base_pos (Vect2d): position de référence de la fenêtre
        """

        pos = pos.copy()

        if base_pos.length() != 0:
            pos = (pos - base_pos)*cls.zoom_factor

        pos = pos.toIntValues()

        font_family = "comicsansms"

        if base_pos.length() != 0:
            size *= cls.zoom_factor

        font_size = int(size)

        if cls.all_font.get(font_family, None) is None:
            # Si la police n'existe pas encore

            cls.all_font[font_family] = {}

        if cls.all_font[font_family].get(size, None) is None:
            # Si la taille de la police n'existe pas encore

            cls.all_font[font_family][font_size] = pygame.font.SysFont(font_family, font_size)
            # On charge la police

        font = cls.all_font[font_family][font_size]
        # On utilise la police

        text = str(text)

        color = [int(color[i]) if color[i] <= 255 else 255 for i in range(len(color))]
        # On veut une couleur avec des nombres entiers

        text_surface = font.render(text, True, color)

        if len(color) == 4 and color[3] != 255:
            # Si la couleur a de la transparence

            alpha_img = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
            alpha_img.fill((255, 255, 255, color[3]))
            text_surface.blit(alpha_img, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        size = Vect2d(text_surface.get_width(), text_surface.get_height())
        pos -= size//2

        cls.window.blit(text_surface, pos.toTuple())

    @classmethod
    def drawLine(cls, pos1: Vect2d, pos2: Vect2d, color: Color, base_pos: Vect2d = Vect2d(0, 0), width: int = 1) -> None:
        """Procédure pour dessiner une ligne à l'écran

        Args:
            pos1 (Vect2d): position de départ
            pos2 (Vect2d): position d'arrivée
            color (Color): couleur de la ligne
            base_pos (Vect2d): position de référence de la fenêtre
            width (int): largeur de la ligne
        """

        pos1 = pos1.copy()
        pos2 = pos2.copy()

        if base_pos.length() != 0:
            pos1 = (pos1 - base_pos)*cls.zoom_factor
            pos2 = (pos2 - base_pos)*cls.zoom_factor

        pos1 = pos1.toIntValues()
        pos2 = pos2.toIntValues()

        if width == 1:
            pygame.gfxdraw.line(cls.window, pos1.x, pos1.y, pos2.x, pos2.y, color)
        else:
            pygame.draw.line(cls.window, color, pos1.toTuple(), pos2.toTuple(), width)

        # pygame.draw.line permet d'avoir une largeur de ligne, mais pygame.gfxdraw.line profite de
        # l'accélération matérielle de la SDL

    @classmethod
    def drawImg(cls, img: pygame.Surface, pos: Vect2d, base_pos: Vect2d = Vect2d(0, 0), radius: int = None) -> None:
        """Procédure pour dessiner une image circulaire à l'écran

        Args:
            img (pygame.Surface): image à dessiner
            pos (Vect2d): position de l'image
            base_pos (Vect2d): position de référence de la fenêtre
            radius (int): rayon désiré de l'image
        """

        pos = (pos - base_pos)*cls.zoom_factor
        pos = pos.toIntValues()

        if radius is not None:
            pos -= Vect2d(radius, radius)
            img = pygame.transform.smoothscale(img, (radius*2, radius*2))
            # On agrandit (ou réduit) la taille de l'image

        cls.window.blit(img, pos.toTuple())

if __name__ == "__main__":
    import time

    pygame.init()

    print("Init")
    Display.init(width=1920, height=1080, start_fullscreen=False, framerate=60)

    print("Cercle")
    Display.drawCircle(Vect2d(100, 100), Color.RED, radius=50)

    print("Texte")
    Display.drawText("Test", Vect2d(800, 600))

    print("Ligne")
    Display.drawLine(Vect2d(200, 300), Vect2d(400, 500), Color.BLUE)

    print("Update 1")
    Display.updateFrame()

    print("Délai 1")
    time.sleep(1)

    print("Update 2")
    Display.updateFrame()

    print("Délai 2")
    time.sleep(1)

    pygame.quit()
