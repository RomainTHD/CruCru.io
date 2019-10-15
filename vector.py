class Vect2d:
    """
    Vecteur à 2 dimensions
    """

    def __init__(self, x:float=0, y:float=0) -> None:
        """
        Constructeur

        INPUT :
            x : int ou float, la composante x, 0 par défaut
            y : int ou float, la composante y, 0 par défaut

        OUTPUT :
            None
        """

        self.x = x
        self.y = y

    def copy(self) -> 'Vect2d':
        """
        Retourne une copie de soi-même

        Exemple :
            u = Vect2d(1, 2)
            v = u.copy()
            # v == u

        INPUT :
            None

        OUTPUT :
            new_vect : Vect2d, une copie de self
        """

        new_vect = Vect2d(self.x, self.y)
        return new_vect

    def __truediv__(self, n:float) -> 'Vect2d':
        """
        Fonction exécutée lors d'une division réelle
        Chaque composante est divisée une à une

        Exemple :
            u = Vect2d(2, 4)
            u = u/2
            # u == Vect2d(1, 2)

        INPUT :
            n : int ou float, le diviseur

        OUTPUT :
            new_vect : Vect2d, le vecteur divisé
        """

        new_vect = self.copy()

        if isinstance(n, (int, float)):
            new_vect.x /= n
            new_vect.y /= n
        else:
            raise ValueError("Not a number")

        return new_vect

    def __add__(self, v:'Vect2d') -> 'Vect2d':
        new_vect = self.copy()

        if isinstance(v, Vect2d):
            new_vect.x += v.x
            new_vect.y += v.y
        else:
            raise ValueError("Not a vector")

        return new_vect

    def __sub__(self, v:'Vect2d') -> 'Vect2d':
        new_vect = self.copy()

        if isinstance(v, Vect2d):
            new_vect.x -= v.x
            new_vect.y -= v.y
        else:
            raise ValueError("Not a vector")

        return new_vect

    def __mul__(self, n:float) -> 'Vect2d':
        new_vect = self.copy()

        if isinstance(n, (int, float)):
            new_vect.x *= n
            new_vect.y *= n
        else:
            raise ValueError("Not a number")

        return new_vect

    def __eq__(self, v:'Vect2d') -> 'Vect2d':
        if isinstance(v, Vect2d):
            if self.x == v.x and self.y == v.y:
                res = True
            else:
                res = False
        else:
            raise ValueError("Not a vector")

        return res

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return "(x:{0},y:{1})".format(self.x, self.y)

    def normalize(self) -> 'Vect2d':
        sum = (self.x**2 + self.y**2)**0.5

        if sum == 0:
            new_vect = Vect2d(0, 0)
        else:
            new_vect = self/sum

        return new_vect

    @classmethod
    def distSq(cls, v1:'Vect2d', v2:'Vect2d') -> float:
        dist = (v1.x - v2.x)**2 + (v1.y - v2.y)**2
        return dist

    @classmethod
    def dist(cls, v1:'Vect2d', v2:'Vect2d') -> float:
        dist = cls.distSq(v1, v2)**0.5
        return dist

    def length(self):
        length = Vect2d.dist(self, Vect2d(0, 0))
        return length

    def lengthSq(self):
        length = Vect2d.distSq(self, Vect2d(0, 0))
        return length

# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
