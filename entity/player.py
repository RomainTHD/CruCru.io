"""Joueur"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.vector import Vect2d

from entity.creature import Creature

class Player(Creature):
    """Créature joueur

    Attributs:
        mouse_pos (Vect2d): position de la souris
    """

    mouse_pos = Vect2d()

    def __init__(self, pos: Vect2d, name: str, color: 'Color', creature_id: int) -> None:
        """Constructeur

        Args:
            pos (Vect2d): position du joueur
            name (str): nom du joueur
            color (Color): couleur du joueur
            creature_id (int): id de la famille du joueur
        """

        super().__init__(pos, name, color, creature_id)

    def update(self, map_size: Vect2d) -> None:
        """Met à jour le joueur

        Args:
            map_size (Vect2d): taille de la map
        """

        if self.mouse_pos.lengthSq() > self.BASE_RADIUS**2:
            coeff_dist_mouse = 1
        else:
            coeff_dist_mouse = self.mouse_pos.length()/self.BASE_RADIUS
            coeff_dist_mouse = coeff_dist_mouse**2

        self.speed = self.mouse_pos.normalize()*coeff_dist_mouse + self.speed*0.95

        self.direction = self.speed.normalize()*coeff_dist_mouse
        self.applySpeed(map_size)
