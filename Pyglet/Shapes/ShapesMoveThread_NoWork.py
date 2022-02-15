import time
import threading
import pyglet


window = pyglet.window.Window()
line = pyglet.shapes.Line(x=0, y=0, x2=20, y2=30, color=(200, 100, 0))
circle = pyglet.shapes.Circle(x=40, y=40, radius=10, color=(0, 255, 0))
rect = pyglet.shapes.Rectangle(x=100, y=100, width=50, height=50, color=(0, 0, 255))


@window.event
def on_draw():
    window.clear()
    line.draw()
    circle.draw()
    rect.draw()


def working():
    while 1:
        # RECT
        rect.x += 1
        rect.y += 1
        rect.width += 1
        rect.height += 1
        # CIRCLE
        circle.x += 1
        circle.y += 1
        # LINE
        line.x2 += 1
        line.y2 += 1
        time.sleep(0.1)


thread = threading.Thread(target=working)
thread.start()

pyglet.app.run()
