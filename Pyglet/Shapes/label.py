import pyglet

game = pyglet.window.Window(640, 480, "I'm a window")

batch = pyglet.graphics.Batch()
pyglet.text.Label('DING', font_name='Arial', font_size=24, x=100, y=100, batch=batch)
pyglet.shapes.Line(x=0, y=0, x2=100, y2=100, width=2, color=(255, 0, 0), batch=batch)


@game.event
def on_draw():
    game.clear()
    batch.draw()


pyglet.app.run()
