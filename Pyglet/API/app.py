import pyglet


window = pyglet.window.Window(width=800, height=600)

event_loop = pyglet.app.EventLoop()


@event_loop.event
def on_window_close(window):
    event_loop.exit()
