from util.vector import Vect2d
from util.color import Color

from view.display import Display

from menu.widget import Widget

class TextArea(Widget):
    def __init__(self, pos, size, text, value, when_display):
        super().__init__(pos, size, text)

        self.value = value

        self.when_display = when_display

def Name_TextArea_Display(text_area, mouse_pos):
    Display.drawRect(text_area.pos,
                     text_area.size,
                     Color.CYAN,
                     fill=False
                     )

    min_size = max(text_area.size.x, text_area.size.y)
    # Taille minimale entre la largeur et la hauteur

    font_size = min_size*5/100

    Display.drawText(text_area.text,
                     Vect2d(text_area.pos.x + text_area.size.x/2,
                            text_area.pos.y + text_area.size.y/10),
                     size=font_size,
                     color=Color.RED
                     )

    font_size = min_size*5/50

    Display.drawText(text_area.value,
                     text_area.pos + text_area.size/2,
                     size=font_size,
                     color=Color.RED
                     )

    return text_area.isMouseOver(mouse_pos)
