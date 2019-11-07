### AJOUTS :
* Division du cercle pour attaquer (split)
* Écran de mort
* Réseau
* Commentaires
* Log

### CORRECTIONS :
* D'abord chercher à vider le carré dans lequel l'ennemi est
 Quand player mort revenir au menu
* HSV -> HSB (ou HSL)
* Config custom (avec par exemple une valeur par défaut, un min, un max) -> cf. VISI201
* Vect2d : héritage de list ?
* Transformer toutes les couleurs en Color (qui hériterait de list)
* Avec les 2 idées précédentes on peut utiliser directement Vect2d et Color en parametre de fonction
* Vect2d : pouvoir le choisir constant ?
* Renommer la variable 'map' dans créature
* Plutôt que BASE_SCORE faire proportionnel

### BUGS :
* Grossisement sur les bords bug de déplacement
* Bug cellule ne pas apparaitre sur le joueur direct
* Cellule à manger apparaissent sur la ligne
* Attention lors de l'apparition ne pas apparaitre à côté d'un joueur imposant sinon on perd direct, aucun intérêt

gota.io

https://docs.python.org/3/library/enum.html
https://docs.python.org/3/library/abc.html
https://docs.python.org/3/library/functions.html?highlight=property#property
