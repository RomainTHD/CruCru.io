import random

class Color:
    RED    = (77 , 0  , 0  )
    ORANGE = (255, 127, 0  )
    YELLOW = (255, 5  , 0  )
    LIME   = (127, 255, 0  )
    GREEN  = (0  , 255, 0  )
    CYAN   = (0  , 255, 255)
    BLUE   = (0  , 0  , 255)
    PURPLE = (127, 0  , 255)
    PINK   = (255, 0  , 255)

    BLACK  = (0  , 0  , 0  )
    GRAY   = (127, 127, 127)
    WHITE  = (255, 255, 255)

    @classmethod
    def randomColor(cls, hue:int=None) -> (int, int, int):
        if hue is None:
            hue = random.randrange(0, 360)

        color = cls.HSVToRGB(hue, 100, 100)

        return color

    @staticmethod
    def HSVToRGB(h:int=0, s:int=100, v:int=100) -> (int, int, int):
        """
        Retourne le code hexadécimal d'une couleur dans l'espace HSV

        INPUT :
            h : int, couleur entre 0 et 360 sur la roue des couleurs
                     0 : rouge, 120 : vert, 260 : bleu, 360 : rouge encore
            s : int, saturation entre 0 et 100, niveau de gris
            v : int, valeur entre 0 et 100, clair ou foncé

        OUTPUT :
            s : tuple, couleur en hexadécimal. Exemple : '#baaaad'
        """

        # Conversion vers RGB

        h /= 360
        s /= 100
        v /= 100

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

        return (r, g, b)

#! avoir objet color ?
