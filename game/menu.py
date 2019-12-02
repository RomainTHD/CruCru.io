if __name__ == "__main__":
    import sys
    sys.path.append("..")

import pygame

from util.vector import Vect2d

from game.button import *
from game.gamestate import GameState
from game.map import Map

from view.display import Display

class Menu:
    @classmethod
    def init(cls):
        cls.applyState(GameState.MENU)
        Display.execWhenResized(cls.createButtons)
    
    @classmethod
    def applyState(cls, state):
        cls.can_play = False
        cls.state = state
        cls.can_quit = False

        print("abcd")
        
        cls.createButtons(Display.size.x, Display.size.y, first_try=True)

    @classmethod
    def play(cls):
        Display.setCursorArrow()
        Map.reset()
        cls.can_play = True

    @classmethod
    def createButtons(cls, width: int, height: int, first_try: bool = False):
        cls.buttons = []
        
        cls.first_try = first_try
        
        print(cls.state)

        if cls.state == GameState.MENU:
            cls.applyMenu(width, height)
        elif cls.state == GameState.WIN:
            cls.applyWin(width, height)
        else:
            cls.applyEnd(width, height)

    @classmethod
    def quit(cls):
        cls.can_quit = True

    @classmethod
    def applyMenu(cls, width, height):
        cls.buttons.append(Button(pos=Vect2d(width/4, height/3),
                                  size=Vect2d(width/2, height/3),
                                  text="Jouer",
                                  on_click=cls.play,
                                  when_display=buttonStart_Display,
                                  when_init=buttonStart_Init))

    @classmethod
    def applyEnd(cls, width, height):
        cls.buttons.append(Button(pos=Vect2d(width/4, height/5),
                                  size=Vect2d(width/2, height/5),
                                  text="Perdu !",
                                  when_display=buttonEnd_Display,
                                  when_init=lambda b: buttonWinOrEnd_Init(b, cls.first_try, Color.RED)))

        cls.buttons.append(Button(pos=Vect2d(width/5, 3*height/5),
                                  size=Vect2d(width/5, height/5),
                                  text="Rejouer",
                                  on_click=cls.play,
                                  when_display=buttonEndChoice_Display,
                                  when_init=lambda b: buttonWinOrEnd_Init(b, cls.first_try, Color.RED)))

        cls.buttons.append(Button(pos=Vect2d(3*width/5, 3*height/5),
                                  size=Vect2d(width/5, height/5),
                                  text="Quitter",
                                  on_click=cls.quit,
                                  when_display=buttonEndChoice_Display,
                                  when_init=lambda b: buttonWinOrEnd_Init(b, cls.first_try, Color.RED)))

    @classmethod
    def applyWin(cls, width, height):
        cls.buttons.append(Button(pos=Vect2d(width/4, height/5),
                                  size=Vect2d(width/2, height/10),
                                  text="Gagné !",
                                  when_display=buttonWin_Display,
                                  when_init=lambda b: buttonWinOrEnd_Init(b, cls.first_try, Color.GREEN)))

        cls.buttons.append(Button(pos=Vect2d(width/5, 3*height/5),
                                  size=Vect2d(width/5, height/5),
                                  text="Rejouer",
                                  on_click=cls.play,
                                  when_display=buttonEndChoice_Display,
                                  when_init=lambda b: buttonWinOrEnd_Init(b, cls.first_try, Color.GREEN)))

        cls.buttons.append(Button(pos=Vect2d(3*width/5, 3*height/5),
                                  size=Vect2d(width/5, height/5),
                                  text="Quitter",
                                  on_click=cls.quit,
                                  when_display=buttonEndChoice_Display,
                                  when_init=lambda b: buttonWinOrEnd_Init(b, cls.first_try, Color.GREEN)))

    @classmethod
    def update(cls, mouse_pos, mouse_pressed):
        cls.mouse_pos = mouse_pos

        if mouse_pressed:
            for i in range(len(cls.buttons)):
                if cls.buttons[i].isMouseOver(cls.mouse_pos):
                    cls.buttons[i].on_click()

    @classmethod
    def display(cls):
        hand_cursor = False

        for i in range(len(cls.buttons)):
            hand_cursor = cls.buttons[i].display(cls.mouse_pos) or hand_cursor

        if hand_cursor:
            Display.setCursorHand()
        else:
            Display.setCursorArrow()

