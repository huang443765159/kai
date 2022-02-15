import pyglet
from pyglet import font
from pyglet import resource


window = pyglet.window.Window(width=500, height=500)

resource.add_font('HWHP.ttf')
action_man = font.load('HWHP')
label = pyglet.text.Label(x=100, y=100, text='你好', font_size=50, font_name='Hello', color=(255, 0, 0, 255))


@window.event
def on_draw():
    window.clear()
    label.draw()


if __name__ == '__main__':
    pyglet.app.run()
