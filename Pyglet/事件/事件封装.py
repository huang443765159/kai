import pyglet
from pyglet.window import *


window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()


class EventHandler:

    def on_key_press(self, symbol, modifiers):
        print(1)

    def on_mouse_press(self, x, y, button, modifiers):
        print(2)


handlers = EventHandler()


def start_game():
    window.push_handlers(handlers)


def stop_game():
    window.pop_handlers()


start_game()
pyglet.app.run()
