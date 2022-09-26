#-*- coding: utf-8 -*-


from asyncio.windows_events import NULL
from random import randint
from tkinter import Widget

from kivy.app import App

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from kivy.config import Config
Config.set("graphics", "height", 480)
Config.set("graphics", "width", 640)

from kivy.properties import StringProperty

from kivy.uix.widget import Widget


resource_add_path("C:\Windows\Fonts")
LabelBase.register(DEFAULT_FONT, "UDDIGIKYOKASHON-R.TTC")

resource_add_path("image")

#App().run()

class ImageWidget(Widget):

    source = StringProperty("image/1.jpg") 

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass


    def buttonStarted(self):

        self.source = "image/1.jpg"

        #return self.source


    def buttonRandom(self):

        self.source = f"image/{randint(1, 10)}.jpg"

        #return self.source


    def TextIn(self):

        self.a = self.ids.text1

        if int(self.a.text) < 1 or 10 < int(self.a.text) :

            self.source = "image/S__15343635.jpg"

            return self.source


        else:
    
            self.source = f"image/{self.a.text}.jpg"

            return self.source


class Cat2App(App):
    def __init__(self, **kwargs):
        super(Cat2App, self).__init__(**kwargs)
        self.title = 'ネコ画像表示'


if __name__=="__main__":
    Cat2App().run()
