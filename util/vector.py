"""
Vecteur à 2 dimensions
"""

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

    def __eq__(self, v: 'Vect2d') -> 'Vect2d':
        """Fonction exécutée lors d'un test d'égalité
        Chaque composante est comparée une à une

        Exemple :
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

        if isinstance(v, Vect2d):
            res = (self.x == v.x and self.y == v.y)
        else:
            raise TypeError(str(type(v)) + " : not a vector")

        return res

    def __repr__(self) -> str:
        """Fonction exécutée pour obtenir la représentation du vecteur en string

        Returns:
            self.__str__()
        """

        return self.__str__()

    def __str__(self) -> str:
        """Fonction exécutée pour obtenir la représentation du vecteur en string

        Returns:
            s (str) : représentation en string
        """

        #!
        # n = 3
        #
        # x = int(self.x*10**n)
        # y = int(self.y*10**n)
        #
        # sx = str(x//10**n) + '.'
        # sy = str(y//10**n) + '.'
        #
        # for i in range(n):
        #     sx += str(int(x*10 - int(x)*10 - x*10%1))
        #
        #     x *= 10

        sx = str(self.x)
        sy = str(self.y)

        s = "(x:" + sx + ",y:" + sy + ")"

        return s

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

        length = Vect2d.distSq(self, Vect2d(0, 0))
        return length

    def length(self):
        """Retourne la norme du vecteur

        Returns:
            length (float): norme
        """

        length = self.lengthSq()**0.5
        return length

#! ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

#! ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
