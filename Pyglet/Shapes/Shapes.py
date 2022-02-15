import pyglet


window = pyglet.window.Window()
line = pyglet.shapes.Line(x=0, y=10, x2=20, y2=30, color=(200, 100, 0))
circle = pyglet.shapes.Circle(x=40, y=40, radius=10, color=(0, 255, 0))
rect = pyglet.shapes.Rectangle(x=100, y=100, width=50, height=50, color=(0, 0, 255))
rect.x = 200
rect.y = 200


@window.event
def on_draw():
    window.clear()
    line.draw()
    circle.draw()
    rect.draw()


pyglet.app.run()
