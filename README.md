# CruCru.io

### Principe du jeu

#### But

Manger les éléments plus petits que soi en évitant ceux plus gros que soi.

#### Comment jouer

* **Menu**
    * Assez explicite dans le jeu

* **Contrôles**
    * Vous contrôlez le joueur à la souris
    * Vous pouvez vous diviser en appuyant sur ```SPACE```
    * Pour quitter, maintenez la touche ```ESC``` enfoncée
    * Pour se mettre en plein écran, c'est la touche ```F11``` qu'il faut enfoncer

#### Comment lancer le jeu

Pour jouer à ce jeu, il vous faudra avoir installé Python (**≥ 3.7**) et pygame
* Ubuntu, Debian :
```Bash
sudo apt-get install python3
python3 -m pip install pygame --user
# ou `pip3 install pygame`
# `--user` est facultatif si vous avez les privilèges requis
```

* Fedora
```Bash
sudo dnf install python3
python3 -m pip install pygame --user
```

* Arch, Manjaro
```Bash
sudo pacman -S python
python -m pip install pygame --user
```

* Windows :
Téléchargez et installez Python 3 [ici](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe) (64 bit) et ajoutez le à la variable d'environnement ```PATH```
```Powershell
python -m pip install pygame --user
# ou `pip install pygame`
```

Vous devrez ensuite exécuter le fichier ```./main.py```, soit par terminal / cmd / Powershell avec ```python main.py``` ou ```python3 main.py``` <br />
Certains paramètres sont modifiables dans le fichier ```./config.py``` <br />
Vous pouvez ajouter des skins dans le dossier ```./data/skins/```, avec éventuellement une description de ce skin dans le dossier ```./data/description/```<br />
Vous pouvez aussi ajouter des noms dans le fichier ```./data/usernames.txt```

### Aperçu

Vous pouvez voir dans la barre de titre le nombre d'images par secondes, qui peut facilement dépasser 300 (si les paramètres l'autorisent) sans que le jeu paraisse plus rapide (plus fluide par contre oui). <br /> 
Dans la fenêtre de jeu nous voyons le joueur au centre, quelques ennemis et de la nourriture (petites boules). <br />
À vous de télécharger notre jeu pour voir les buissons :kissing_heart:

![Aperçu de l'image](data/preview.png)

### Licence

GPL-3.0-or-later

### Crédits

Romain THEODET (@Rominos111) <br />
Sarah CRUMIERE (@crumiers)

Projet VISI301, L2 CMI INFO + MATHS, USMB, 2019
