import random

class Color:
    red    = (255, 0  , 0  )
    orange = (255, 127, 0  )
    yellow = (255, 255, 0  )
    lime   = (127, 255, 0  )
    green  = (0  , 255, 0  )
    cyan   = (0  , 255, 255)
    blue   = (0  , 0  , 255)
    purple = (127, 0  , 255)
    pink   = (255, 0  , 255)

    black  = (0  , 0  , 0  )
    gray   = (127, 127, 127)
    white  = (255, 255, 255)

    all_color = (red, orange, yellow, lime, green, cyan, blue, purple, pink)

    @classmethod
    def couleurAleatoire(cls):
        n = random.randrange(0, len(cls.all_color))

        return cls.all_color[n]
