import pyglet.app
from pyglet.gl import *


window = pyglet.window.Window()
batch = pyglet.graphics.Batch()
vertex_list = batch.add(2, pyglet.gl.GL_POINTS, None,
                        ('v2i', (100, 100, 200, 200)),
                        ('c3B', (0, 0, 255, 255, 0, 0))
                        )


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.app.run()
