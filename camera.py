from vector import Vect2d

class Camera:
    pos = Vect2d()
    window_pos = Vect2d()

    @classmethod
    def setWindowSize(cls, width:int, height:int):
        cls.window_pos = Vect2d(width, height)/2

    @classmethod
    def setPos(cls, pos:Vect2d) -> None:
        cls.pos = pos - cls.window_pos
