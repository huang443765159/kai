import pyglet
from pyglet.window import *


window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()


class ClankWidget(pyglet.event.EventDispatcher):
    def clank(self):
        self.dispatch_event('on_clank')

    def click(self, clicks):
        self.dispatch_event('on_clicked', clicks)

    def on_clank(self):
        print('Default clank handler')


ClankWidget.register_event_type('on_clank')
ClankWidget.register_event_type('on_clicked')

widget = ClankWidget()


@widget.event
def on_clank():
    print(1)


@widget.event
def on_clicked(clicks):
    print(2)


def override_on_clicked(clicks):
    print(3)


widget.push_handlers(on_clicked=override_on_clicked)
pyglet.app.run()
