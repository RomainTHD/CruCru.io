"""Couleurs"""

import random

class Color:
    """Classe pour gérer l'organisation des couleurs
    Contient des attributs statiques qui sont des constantes de couleurs

    Attributs:
        RED, ORANGE, YELLOW, ... (tuple): triplet de couleurs dans l'espace RGB
    """

    RED = (255, 0, 0)
    ORANGE = (255, 127, 0)
    YELLOW = (255, 255, 0)
    LIME = (127, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (127, 0, 255)
    PINK = (255, 0, 255)

    BLACK = (0, 0, 0)
    DARK_GRAY = (63, 63, 63)
    GRAY = (127, 127, 127)
    LIGHT_GRAY = (191, 191, 191)
    WHITE = (255, 255, 255)
    
    BUISSON_COLOR = (0, 255, 0)

    TRANSPARENT = (255, 255, 255, 0)
    TO_TRANSPARENT = (99, 28, 11)
    # Cette valeur est une valeur très particulière : elle est en effet remplacée par de la
    # transparence lors de l'affichage à l'écran

    @staticmethod
    def randomColor() -> (int, int, int):
        """Retourne une couleur aléatoire dans l'espace RGB
        Pour cela, on passe d'abord dans l'espace HSV (teinte, saturation, valeur)
        Cet espace permet de choisir des couleurs très vives

        Returns:
            color (tuple of 4 int): tuple avec les composantes RGB
        """

        hue = random.randrange(0, 360)
        # Teinte aléatoire

        color = Color.HSVToRGB(hue, 100, 100)
        # On passe de HSV à RGB

        return color

    @staticmethod
    def oppositeColor(color: tuple):
        hsv_color = Color.RGBToHSV(*color)

        new_color = Color.HSVToRGB(hsv_color[0]+180, *hsv_color[1:])

        return new_color

    @staticmethod
    def RGBToHSV(r: int, g: int, b: int, a: int = 255) -> (int, int, int, int):
        r /= 255
        g /= 255
        b /= 255

        mx = max(r, g, b)
        mn = min(r, g, b)

        df = mx-mn

        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        elif mx == b:
            h = (60 * ((r-g)/df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = (df/mx)*100

        v = mx*100

        h = int(h)
        s = int(s)
        v = int(v)

        return (h, s, v, a)

    @staticmethod
    def HSVToRGB(h: int, s: int = 100, v: int = 100, a: int = 255) -> (int, int, int, int):
        """Retourne le code RGB d'une couleur dans l'espace HSV

        Args:
            h (int): couleur entre 0 et 360
                     0 : rouge, 120 : vert, 260 : bleu, 360 : rouge encore
            s (int): saturation entre 0 et 100, niveau de gris
            v (int): luminosité entre 0 et 100, clair ou foncé
            a (int): opacité entre 0 et 255, transparent ou opaque

        Returns:
            s (tuple of 4 int): couleurs RGBA entre 0 et 255
        """

        while h < 0:
            h += 360*100
        h %= 360
        h /= 360

        while s < 0:
            s += 101*100
        s %= 101
        s /= 100

        while v < 0:
            v += 101*100
        v %= 101
        v /= 100

        # Pour avoir des valeurs entre 0 et 1

        if s == 0:
            r = g = b = int(v*255)
        else:
            i = int(h*6)
            f = (h*6)-i
            p = int(255*v*(1-s))
            q = int(255*v*(1-s*f))
            t = int(255*v*(1-s*(1-f)))

            v = int(v*255)

            i %= 6

            if i == 0:
                r, g, b = (v, t, p)
            elif i == 1:
                r, g, b = (q, v, p)
            elif i == 2:
                r, g, b = (p, v, t)
            elif i == 3:
                r, g, b = (p, q, v)
            elif i == 4:
                r, g, b = (t, p, v)
            elif i == 5:
                r, g, b = (v, p, q)

        return (r, g, b, a)
