from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import stencil_instructions

class Card:
    class CardView(Widget):
        def prepare(self):
            with self.canvas:
                Color(rgb=get_color_from_hex('#F2F3FB'))
                RoundedRectangle(pos=self.pos, size=(250, 200), radius=[15])

    class Border(Widget):
        def prepare(self):
            with self.canvas:
                Color(rgb=get_color_from_hex('#150470'))
                RoundedRectangle(pos=self.pos, size=self.size, radius=[55])

    class Circle(Image):
        def prepare(self):
            with self.canvas.before:
                stencil_instructions.StencilPush()
                RoundedRectangle(pos=(self.x + 5, self.y + 5), size=(100, 100), size_hint=(None, None), radius=[50])
                stencil_instructions.StencilUse()
            with self.canvas.after:
                stencil_instructions.StencilUnUse()
                stencil_instructions.StencilPop()


    def circular_image(self, pos, size):
        card_x, card_y = pos
        card_width, card_height = size

        x = card_x + card_width - (110 + 10)
        y = card_y + card_height - (110 + 10)

        border = self.Border(pos=(x, y), size=(110, 110))
        border.prepare()

        circle = self.Circle(source='corgi.jpg', pos=border.pos)
        if circle.image_ratio < 1:
            circle.size_hint = (circle.image_ratio + 1, circle.image_ratio + 1)
        else:
            circle.size_hint = (circle.image_ratio, circle.image_ratio)
        circle.prepare()

        anchor_layout = AnchorLayout(pos=border.pos, anchor_x='center', anchor_y='center', padding=0, size=border.size)
        anchor_layout.add_widget(circle)

        border.add_widget(anchor_layout)

        return border

    def build(self):
        card_view = self.CardView(pos=(0, 0), size=(250, 200))
        card_view.prepare()
        card_view.add_widget(self.circular_image(card_view.pos, card_view.size))
        return card_view
