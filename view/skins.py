import os
import pygame

class Skins:
    @classmethod
    def loadAll(cls):
        cls.all_skins = []

        path = "../data/skins/"

        all_file_path = os.listdir(path)

        all_img = []

        for i in range(len(all_file_path)):
            extension = all_file_path[i].split('.')[-1]

            if extension in ("png", "jpg"):
                img = pygame.image.load(path + all_file_path[i])

                all_img.append(img)

        img = all_img[0]
        crop = (0, 0, 10, 10)
        cropped = img.subsurface(crop)

Skins.loadAll()





import pygame
import pygame.gfxdraw

ATOM_IMG = pygame.Surface((30, 30), pygame.SRCALPHA)
# draw.circle is not anti-aliased and looks rather ugly.
# pygame.draw.circle(ATOM_IMG, (0, 255, 0), (15, 15), 15)
# gfxdraw.aacircle looks a bit better.
pygame.gfxdraw.aacircle(ATOM_IMG, 15, 15, 14, (0, 255, 0))
pygame.gfxdraw.filled_circle(ATOM_IMG, 15, 15, 14, (0, 255, 0))

class Atom(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ATOM_IMG
        self.rect = self.image.get_rect(center=(150, 200))

pygame.init()
window = pygame.display.set_mode((1000, 1000))

a = Atom()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    pygame.draw.rect(window, (255, 255, 255), (0, 0, 1000, 1000))
    pygame.draw.rect(window, (0, 0, 0), a.rect)
