import pyglet
from pyglet import gl


window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
                         ('v2i', (100, 150, 200, 300)))  # 点的两个坐标, 2D int 型
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
                         ('v3f', (10.0, 15.0, 0.0, 30.0, 35.0, 0.0)))  # 点的2个坐标 + 顶点？没看懂，float型
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
                         ('v2i', (10, 15, 30, 35)),
                         ('c3B', (0, 0, 255, 0, 255, 0))
                         )
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', (100, 100,
                                          150, 100,
                                          200, 200,
                                          250, 300))
                                 )  # 第一个100， 100 为顶点位置


pyglet.app.run()
