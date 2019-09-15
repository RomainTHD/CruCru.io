if __name__ == "__main__":
    raise ImportError("Executez main.py")

import pygame
import time

class Display:
    @classmethod
    def init(cls, dimension:tuple) -> None:
        pygame.init()

        cls.width, cls.height = dimension

        cls.window = pygame.display.set_mode((cls.width, cls.height))

        cls.quit = False

        cls.framerate = 60

    @classmethod
    def bind(cls, key, function):
        pass

    @classmethod
    def exit(cls):
        cls.quit = True

    @classmethod
    def update(cls):
        pass

    @classmethod
    def display(cls):


    @classmethod
    def run(cls):
        while not cls.quit:
            cls.update()
            cls.display()

            pygame.display.flip()

            time.sleep(1/cls.framerate)
