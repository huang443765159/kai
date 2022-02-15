import pyglet
from pyglet.gl import *


window = pyglet.window.Window()


@window.event
def on_draw():
    # window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)  # 3个坐标点
    glVertex2f(window.width, 0)
    glVertex2f(window.width, window.height)
    glEnd()


pyglet.app.run()
