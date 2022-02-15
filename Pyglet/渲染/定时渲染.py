import pyglet


window = pyglet.window.Window()
circle = pyglet.shapes.Circle(x=100, y=100, radius=20, color=(255, 0, 0))
fps_window = pyglet.window.FPSDisplay(window=window)  # 显示fps


@window.event
def on_draw():
    window.clear()
    circle.draw()
    fps_window.draw()


def update(dt):
    circle.x += 1


pyglet.clock.schedule_interval(update, 1 / 10)  # 循环
pyglet.clock.schedule(update)  # 高频率运行，占用CPU
pyglet.clock.schedule_once(update, 0.5)  # 0.5s后刷新一次
pyglet.app.run()
