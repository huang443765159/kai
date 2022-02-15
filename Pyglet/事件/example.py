import pyglet
from pyglet.window import *


window = pyglet.window.Window()


@window.event  # 重新设置大小事件
def on_resize(width, height):
    print(1)


@window.event  # 键盘事件
def on_key_press(symbol, modifiers):
    print(2)
    if symbol == key.SPACE:
        print(3)


@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x, y, button, modifiers)


@window.event
def on_draw():
    window.clear()


pyglet.app.run()
