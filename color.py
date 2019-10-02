import random

class Color:
    """
    Classe pour gérer l'organisation des couleurs
    Contient des attributs statiques qui sont des constantes de couleurs
    """
    
    RED    = (255, 0  , 0  )
    ORANGE = (255, 127, 0  )
    YELLOW = (255, 255, 0  )
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
    def randomColor(cls) -> (int, int, int):
        """
        Retourne une couleur aléatoire dans l'espace RGB
        Pour cela, on passe d'abord dans l'espace HSV (teinte, saturation, valeur)
        Cet espace permet de choisir des couleurs très vives

        INPUT :
            None
        
        OUTPUT :
            color : tuple de int, un tuple avec les composantes RGB
        """
        
        hue = random.randrange(0, 360)
        # Teinte aléatoire

        color = cls.HSVToRGB(hue, 100, 100)
        # On passe de HSV à RGB

        return color

    @staticmethod
    def HSVToRGB(h:int=0, s:int=100, v:int=100) -> (int, int, int):
        """
        Retourne le code RGB d'une couleur dans l'espace HSV

        INPUT :
            h : int, couleur entre 0 et 360
                     0 : rouge, 120 : vert, 260 : bleu, 360 : rouge encore
            s : int, saturation entre 0 et 100, niveau de gris
            v : int, valeur entre 0 et 100, clair ou foncé

        OUTPUT :
            s : tuple de int, tuple de couleurs RGB entre 0 et 255
        """

        h /= 360
        s /= 100
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

        return (r, g, b)
