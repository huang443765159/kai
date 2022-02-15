import pyglet


window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()


event_loop = pyglet.app.EventLoop()


@event_loop.event
def on_window_close(window):
    event_loop.exit()
    return pyglet.event.EVENT_HANDLED


while True:
    pyglet.clock.tick()
    for window in pyglet.app.windows:
        window.switch_to()
        window.dispatch_events()
        window.dispatch_event('on_draw')
        window.flip()


# event_loop.run()
