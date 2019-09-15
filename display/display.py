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

        cls.key_to_function = {}
        cls.str_to_key = {}

    @classmethod
    def bindKey(cls, key, function):
        cls.key_to_function[key] = function

    @classmethod
    def exit(cls):
        cls.quit = True

    @classmethod
    def update(cls):
        pass

    @classmethod
    def display(cls):
        pass

    @classmethod
    def run(cls):
        while not cls.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cls.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

            cls.update()
            cls.display()

            pygame.display.flip()

            time.sleep(1/cls.framerate)

Display.init((1000, 1000))
Display.run()
