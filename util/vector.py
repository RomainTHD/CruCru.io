"""
Vecteur à 2 dimensions
"""

import math

class Vect2d:
    """Vecteur à 2 dimensions

    Attributs:
        x (int): composante horizontale du vecteur
        y (int): composante verticale du vecteur
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """Constructeur

        Args:
            x (int or float, optional): la composante x, 0 par défaut
            y (int or float, optional): la composante y, 0 par défaut
        """

        self.x = x
        self.y = y

    def __truediv__(self, n: float) -> 'Vect2d':
        """Fonction exécutée lors d'une division réelle
        Chaque composante est divisée une à une

        Exemple:
            u = Vect2d(2, 4)
            u = u/2
            assert u == Vect2d(1, 2)

        Args:
            n (int or float): le diviseur

        Returns:
            new_vect (Vect2d): le vecteur divisé

        Raises:
            TypeError: si autre chose qu'un nombre est donné en diviseur
        """

        new_vect = self.copy()

        if isinstance(n, (int, float)):
            new_vect.x /= n
            new_vect.y /= n
        else:
            raise TypeError(str(type(n)) + " : not a number")

        return new_vect

    def __itruediv__(self, n: float) -> 'Vect2d':
        """Fonction exécutée lors d'une division réelle sur soi-même
        Chaque composante est divisée une à une

        Exemple:
            u = Vect2d(2, 4)
            u /= 2
            assert u == Vect2d(1, 2)

        Args:
            n (int or float): le diviseur

        Raises:
            TypeError: si autre chose qu'un nombre est donné en diviseur
        """

        if isinstance(n, (int, float)):
            self.x /= n
            self.y /= n
        else:
            raise TypeError(str(type(n)) + " : not a number")

        return self

    def __floordiv__(self, n: float) -> 'Vect2d':
        """Fonction exécutée lors d'une division entière
        Chaque composante est divisée une à une

        Exemple:
            u = Vect2d(2, 4)
            u = u//3
            assert u == Vect2d(0, 1)

        Args:
            n (int or float): le diviseur

        Returns:
            new_vect (Vect2d): le vecteur divisé

        Raises:
            TypeError: si autre chose qu'un nombre est donné en diviseur
        """

        new_vect = self.copy()

        if isinstance(n, (int, float)):
            new_vect.x //= n
            new_vect.y //= n
        else:
            raise TypeError(str(type(n)) + " : not a number")

        return new_vect

    def __ifloordiv__(self, n: float) -> 'Vect2d':
        """Fonction exécutée lors d'une division entière sur soi-même
        Chaque composante est divisée une à une

        Exemple:
            u = Vect2d(2, 4)
            u //= 3
            assert u == Vect2d(0, 1)

        Args:
            n (int or float): le diviseur

        Raises:
            TypeError: si autre chose qu'un nombre est donné en diviseur
        """

        if isinstance(n, (int, float)):
            self.x //= n
            self.y //= n
        else:
            raise TypeError(str(type(n)) + " : not a number")

        return self

    def __add__(self, v: 'Vect2d') -> 'Vect2d':
        """Fonction exécutée lors d'une addition
        Chaque composante est additionnée une à une

        Exemple:
            u = Vect2d(2, 4)
            v = Vect2d(1, 5)
            w = u + v
            assert w == Vect2d(3, 9)

        Args:
            v (Vect2d): le vecteur à additionner

        Returns:
            new_vect (Vect2d): le vecteur additionné

        Raises:
            TypeError: en cas d'addition avec autre chose qu'un vecteur Vect2d
        """

        new_vect = self.copy()

        if isinstance(v, Vect2d):
            new_vect.x += v.x
            new_vect.y += v.y
        else:
            raise TypeError(str(type(v)) + " : not a vector")

        return new_vect

    def __iadd__(self, v: 'Vect2d') -> 'Vect2d':
        """Fonction exécutée lors d'une addition sur soi-même
        Chaque composante est additionnée une à une

        Exemple:
            u = Vect2d(2, 4)
            v = Vect2d(1, 5)
            u += v
            assert u == Vect2d(3, 9)

        Args:
            v (Vect2d): le vecteur à additionner

        Raises:
            TypeError: en cas d'addition avec autre chose qu'un vecteur Vect2d
        """

        if isinstance(v, Vect2d):
            self.x += v.x
            self.y += v.y
        else:
            raise TypeError(str(type(v)) + " : not a vector")

        return self

    def __sub__(self, v: 'Vect2d') -> 'Vect2d':
        """Fonction exécutée lors d'une soustraction
        Chaque composante est soustraite une à une

        Exemple:
            u = Vect2d(2, 4)
            v = Vect2d(1, 1)
            w = u - v
            assert w == Vect2d(1, 3)

        Args:
            v (Vect2d): le vecteur à soustraire

        Returns:
            new_vect (Vect2d): le vecteur après la soustraction

        Raises:
            TypeError: en cas de soustraction avec autre chose qu'un vecteur Vect2d
        """

        new_vect = self.copy()

        if isinstance(v, Vect2d):
            new_vect.x -= v.x
            new_vect.y -= v.y
        else:
            raise TypeError(str(type(v)) + " : not a vector")

        return new_vect

    def __isub__(self, v: 'Vect2d') -> 'Vect2d':
        """Fonction exécutée lors d'une soustraction sur soi-même
        Chaque composante est soustraite une à une

        Exemple:
            u = Vect2d(2, 4)
            v = Vect2d(1, 1)
            u -= v
            assert u == Vect2d(1, 3)

        Args:
            v (Vect2d): le vecteur à soustraire

        Raises:
            TypeError: en cas de soustraction avec autre chose qu'un vecteur Vect2d
        """

        if isinstance(v, Vect2d):
            self.x -= v.x
            self.y -= v.y
        else:
            raise TypeError(str(type(v)) + " : not a vector")

        return self

    def __mul__(self, n: float) -> 'Vect2d':
        """Fonction exécutée lors d'une multiplication
        Chaque composante est multipliée une à une

        Exemple:
            u = Vect2d(2, 4)
            v = u * 3
            assert v == Vect2d(6, 12)

        Args:
            n (int or float): le coefficient de multiplication

        Returns:
            new_vect (Vect2d): le vecteur multiplié

        Raises:
            TypeError: en cas de multiplication avec autre chose qu'un nombre
        """

        new_vect = self.copy()

        if isinstance(n, (int, float)):
            new_vect.x *= n
            new_vect.y *= n
        else:
            raise TypeError(str(type(n)) + " : not a number")

        return new_vect

    def __imul__(self, n: float) -> 'Vect2d':
        """Fonction exécutée lors d'une multiplication sur soi-même
        Chaque composante est multipliée une à une

        Exemple:
            u = Vect2d(2, 4)
            u *= 3
            assert u == Vect2d(6, 12)

        Args:
            n (int or float): le coefficient de multiplication

        Raises:
            TypeError: en cas de multiplication avec autre chose qu'un nombre
        """

        if isinstance(n, (int, float)):
            self.x *= n
            self.y *= n
        else:
            raise TypeError(str(type(n)) + " : not a number")

        return self

    def __eq__(self, v: 'Vect2d') -> 'Vect2d':
        """Fonction exécutée lors d'un test d'égalité
        Chaque composante est comparée une à une

        Exemple:
            u = Vect2d(2, 4)
            v = Vect2d(2, 4)
            assert u == v

        Args:
            v (Vect2d): le vecteur à comparer

        Returns:
            res (bool): si les 2 vecteurs sont identiques ou non

        Raises:
            TypeError: en cas de test d'égalité avec autre chose qu'un vecteur Vect2d
        """

        precision = 10**9

        if isinstance(v, Vect2d):
            res = (int(self.x*precision) == int(v.x*precision)
                   and int(self.y*precision) == int(v.y*precision))
        else:
            raise TypeError(str(type(v)) + " : not a vector")

        return res

    def __repr__(self) -> str:
        """Fonction exécutée pour obtenir la représentation du vecteur
        Normalement, eval(repr(obj)) == obj

        Exemple:
            u = Vect2d(1, 2)
            assert repr(u) == "Vect2d(1, 2)"

        Returns:
            rep (str): représentation
        """

        rep = "Vect2d({0}, {1})".format(self.x, self.y)

        return rep

    def __str__(self) -> str:
        """Fonction exécutée pour obtenir la représentation du vecteur en string

        Returns:
            s (str) : représentation en string
        """

        sx = str(self.x)
        sy = str(self.y)

        s = "(x:" + sx + ",y:" + sy + ")"

        return s

    def copy(self) -> 'Vect2d':
        """Retourne une copie de soi-même

        Exemple:
            u = Vect2d(1, 2)
            v = u.copy()
            assert u == v

        Returns:
            new_vect (Vect2d): une copie de self
        """

        new_vect = Vect2d(self.x, self.y)

        return new_vect

    def toIntValues(self):
        """Fonction permettant de transformer les composantes en entier 'int'

        Exemple:
            u = Vect2d(2.2, 4.9)
            u = u.toIntValues()
            assert u == Vect2d(2, 4)

        Returns:
            new_vect (Vect2d): le vecteur entier
        """

        new_vect = self.copy()

        new_vect.x = int(new_vect.x)
        new_vect.y = int(new_vect.y)

        return new_vect

    def toTuple(self):
        """Fonction permettant de transformer le vecteur en tuple

        Exemple:
            u = Vect2d(2, 4)
            v = u.toTuple()
            assert v == (2, 4)

        Returns:
            vect_tuple (tuple): le tuple associé au vecteur
        """

        vect_tuple = (self.x, self.y)

        return vect_tuple

    def normalize(self) -> 'Vect2d':
        """Normalise un vecteur pour qu'il ait une taille de 1

        Returns:
            new_vect (Vect2d): nouveau vecteur normalisé
        """

        sum_coords = (self.x**2 + self.y**2)**0.5

        if sum_coords == 0:
            new_vect = Vect2d(0, 0)
        else:
            new_vect = self/sum_coords

        return new_vect

    @classmethod
    def distSq(cls, v1: 'Vect2d', v2: 'Vect2d') -> float:
        """Retourne la distance au carré entre 2 vecteurs
        Utile pour des comparaisons rapides car n'utilise pas la racine carrée

        Exemple:
            u = Vect2d(2, 4)
            v = Vect2d(3, 3)
            w = Vect2d(1, 1)
            Vect2d.distSq(u, v) == Vect2d.distSq(u, w)

        Returns:
            dist (float): distance au carré
        """

        dist = (v1.x - v2.x)**2 + (v1.y - v2.y)**2
        return dist

    @classmethod
    def dist(cls, v1: 'Vect2d', v2: 'Vect2d') -> float:
        """Retourne la distance entre 2 vecteurs

        Returns:
            dist (float): distance
        """

        dist = cls.distSq(v1, v2)**0.5
        return dist

    def lengthSq(self):
        """Retourne la norme au carré du vecteur
        Utile pour des comparaisons rapides car n'utilise pas la racine carrée

        Exemple:
            u = Vect2d(2, 4)
            v = Vect2d(3, 3)
            u.lengthSq() == v.lengthSq()

        Returns:
            length (float): norme au carré
        """

        if self.x == 0 and self.y == 0:
            length = 0
        else:
            length = Vect2d.distSq(self, Vect2d(0, 0))

        return length

    def length(self):
        """Retourne la norme du vecteur

        Returns:
            length (float): norme
        """

        if self.x == 0 and self.y == 0:
            length = 0
        else:
            length = self.lengthSq()**0.5

        return length

    @staticmethod
    def dotProduct(v1: 'Vect2d', v2: 'Vect2d'):
        return v1.x*v2.x + v1.y*v2.y

    @staticmethod
    def angleBetween(v1: 'Vect2d', v2: 'Vect2d'):
        v1 = v1.copy().normalize()
        v2 = v2.copy().normalize()

        angle = 0

        angle = Vect2d.dotProduct(v1, v2) / (v1.length()*v2.length())

        if angle > 1:
            angle = 1

        angle = math.acos(angle)
        angle = math.degrees(angle)

        return angle

if __name__ == "__main__":
    print("__truediv__")
    u = Vect2d(1, 2)
    w = Vect2d(0.5, 1)
    assert u/2 == w

    print("__itruediv__")
    u = Vect2d(1, 2)
    w = Vect2d(0.5, 1)
    u /= 2
    assert u == w

    print("__floordiv__")
    u = Vect2d(2, 4)
    u = u//3
    assert u == Vect2d(0, 1)

    print("__ifloordiv__")
    u = Vect2d(2, 4)
    u //= 3
    assert u == Vect2d(0, 1)

    print("__add__")
    u = Vect2d(1, 2)
    v = Vect2d(3, 3)
    w = Vect2d(4, 5)
    assert u+v == w

    print("__iadd__")
    u = Vect2d(1, 2)
    u += Vect2d(3, 3)
    w = Vect2d(4, 5)
    assert u == w

    print("__sub__")
    u = Vect2d(1, 2)
    v = Vect2d(3, 3)
    w = Vect2d(-2, -1)
    assert u-v == w

    print("__isub__")
    u = Vect2d(1, 2)
    u -= Vect2d(3, 3)
    w = Vect2d(-2, -1)
    assert u == w

    print("__mul__")
    u = Vect2d(1, 2)
    w = Vect2d(2, 4)
    assert u*2 == w

    print("__imul__")
    u = Vect2d(1, 2)
    u *= 2
    w = Vect2d(2, 4)
    assert u == w

    print("__eq__")
    u = Vect2d(1, 2)
    w = Vect2d(1, 2)
    assert u == w

    print("__repr__")
    u = Vect2d(1, 2)
    print(repr(u))
    assert repr(u) == "Vect2d(1, 2)"

    print("__str__")
    u = Vect2d(1, 2)
    print(u)

    print("copy")
    u = Vect2d(1, 2)
    v = u.copy()
    assert u == v

    print("toIntValues")
    u = Vect2d(1.2, 3.9)
    v = u.toIntValues()
    assert v.x == 1 and v.y == 3

    print("normalize")
    u = Vect2d(1, 1)
    v = Vect2d(3, 3)
    assert u.normalize() == v.normalize()

    print("dist & distSq")
    u = Vect2d(2, 4)
    v = Vect2d(3, 3)
    w = Vect2d(4, 4)
    assert Vect2d.distSq(u, v) == Vect2d.distSq(v, w)
    assert int(10**9*Vect2d.dist(u, v)**2)/10**9 == Vect2d.distSq(u, v)

    print("length & lengthSq")
    u = Vect2d(2, 4)
    v = Vect2d(4, 8)
    assert u.lengthSq()*4 == v.lengthSq()
    u = Vect2d(2, 2)
    assert int(10**9*u.length()**2)/10**9 == u.lengthSq()
    assert u.lengthSq() == 8
    v = Vect2d(3, 3)
    assert u.lengthSq() != v.lengthSq()

#! ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

#! ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#! __contains__, keys, items, values, get, __getitem__, __len__, __iter__
#! __getitem__(), __setitem__(), __delitem__()
#! append(), count(), index(), extend(), insert(), pop(), remove(), reverse(), sort()
