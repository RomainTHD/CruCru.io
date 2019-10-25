if __name__ == "__main__":
    import sys
    sys.path.append("..")

import pygame

from util.vector import Vect2d

from game.button import Button

from view.display import Display

class Menu:
    can_play = False

    buttons = []

    @classmethod
    def play(cls):
        cls.can_play = True

    @classmethod
    def init(cls, width, height):
        Display.executeWhenResized(cls.whenResized)
        cls.buttons.append(Button(width/4, height/3, width/2, height/3, text="Jouer !", on_click=cls.play))

    @classmethod
    def update(cls, mouse_pos, mouse_pressed):
        cls.mouse_pos = mouse_pos

        if mouse_pressed:
            for i in range(len(cls.buttons)):
                if cls.buttons[i].isMouseOver(cls.mouse_pos):
                    cls.buttons[i].on_click()

    @classmethod
    def display(cls):
        for i in range(len(cls.buttons)):
            cls.buttons[i].display(cls.mouse_pos)

    @classmethod
    def whenResized(cls, width, height):
        for i in range(len(cls.buttons)):
            cls.buttons[i].pos.x = width/4
            cls.buttons[i].pos.y = height/3

            cls.buttons[i].size.x = width/2
            cls.buttons[i].size.y = height/3
