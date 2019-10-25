from util.vector import Vect2d

from view.display import Display

from util.color import Color

class Button:
    def __init__(self, x, y, width, height, text, on_click):
        self.pos = Vect2d(x, y)
        self.size = Vect2d(width, height)

        self.on_click = on_click

        self.color_hue = 0
        self.text = text

    def isMouseOver(self, mouse_pos):
        res = False

        if mouse_pos.x > self.pos.x and mouse_pos.x < self.pos.x + self.size.x:
            if mouse_pos.y > self.pos.y and mouse_pos.y < self.pos.y + self.size.y:
                res = True

        return res

    def display(self, mouse_pos):
        if self.isMouseOver(mouse_pos):
            self.color_hue += 3
        else:
            self.color_hue -= 1

        color = Color.HSVToRGB(self.color_hue)

        min_size = max(self.size.x, self.size.y)

        font_size = min_size*50/400

        Display.drawRect(self.pos, self.size, color, fill=True)
        Display.drawText(self.text, self.pos + self.size/2, Color.BLACK, size=font_size)
