class Vect2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def copy(self):
        new_vect = Vect2d(self.x, self.y)
        return new_vect

    def __truediv__(self, n):
        new_vect = self.copy()

        if isinstance(n, (int, float)):
            new_vect.x /= n
            new_vect.y /= n
        else:
            raise ValueError("Not a number")

        return new_vect

    def __add__(self, v):
        new_vect = self.copy()

        if isinstance(v, Vect2d):
            new_vect.x += v.x
            new_vect.y += v.y
        else:
            raise ValueError("Not a vector")

        return new_vect

    def __sub__(self, v):
        return self.__add__(v*-1)

    def __mul__(self, n):
        new_vect = self.copy()

        if isinstance(n, (int, float)):
            new_vect.x *= n
            new_vect.y *= n
        else:
            raise ValueError("Not a number")

        return new_vect

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(x:{0},y:{1})".format(self.x, self.y)

    def normalize(self):
        sum = (self.x**2 + self.y**2)**0.5

        new_vect = self/sum

        return new_vect

    @classmethod
    def distSq(cls, v1, v2):
        dist = (v1.x - v2.x)**2 + (v1.y - v2.y)**2
        return dist

['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
