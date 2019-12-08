### AJOUTS :
* Faire tableau des meilleurs scores
* Monde infini
* Demander nom joueur
* Serveur

### CORRECTIONS :
* Threads IA
* D'abord chercher à vider le carré dans lequel l'ennemi est
* HSV -> HSB (ou HSL)
* Config custom (avec par exemple une valeur par défaut, un min, un max) -> cf. VISI201
* Vect2d : héritage de list ?
* Transformer toutes les couleurs en Color (qui hériterait de list)
* Avec les 2 idées précédentes on peut utiliser directement Vect2d et Color en parametre de fonction
* Vect2d : pouvoir le choisir constant ?

### BUGS :
* F11 fin de jeu
* Ennemis qui se chevauchent parfois
* Ennemis qui tapent les bords
* Rotation dans le sens des aiguilles d'une montre
* Si target dans coin alors hunter l'aura jamais et va bug dessus
* Ennemis bizarres
* Écran de win
* Size marche mal

gota.io

https://docs.python.org/3/library/enum.html
https://docs.python.org/3/library/abc.html
https://docs.python.org/3/library/functions.html?highlight=property#property

enemy.py
button.py
game.py
map.py
