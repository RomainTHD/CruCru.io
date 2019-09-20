import pygame
import time

from player import Player


player = Player()

red    = (255, 0  , 0  )
green  = (0  , 255, 0  )
blue   = (0  , 0  , 255)
black  = (0  , 0  , 0  )
yellow = (255, 255, 0  )

pygame.init()
# On initialise pygame

window_resolution = (800, 600)
window = pygame.display.set_mode((window_resolution))
# Taille de la fenêtre et création d'une variable fenêtre (window)

pygame.display.set_caption("Agar.io")
# On change le titre

window.fill(black)
# La fenêtre aura un fond noir
# black a été défini plus tôt dans le programme

# rectangle = pygame.Rect(50, 50, 100, 100)
# pygame.draw.rect(window, red, rectangle)
# On crée un objet rectangle en (x=50, y=50) de largeur 100 et de hauteur 100
# ici c'est donc un carré
# la coordonnée (50, 50) correspond au coin en haut à gauche

pygame.display.flip()
# On actualise la fenêtre

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            # Détection de la fermeture de la fenêtre

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                # Détection de la touche échap

    mx, my = pygame.mouse.get_pos()
    # Position (x, y) de la souris

    if pygame.mouse.get_focused():
        # Si souris dans fenêtre
        # print(mx, my)
        pass

    player.update(mx, my)

    time.sleep(1/100)
    # Pour actualiser la fenêtre tous les centième de seconde

    window.fill(black)

    player.display(window)

    pygame.display.flip()

pygame.quit()
