import pyglet
from datetime import datetime

WIDTH = 960
HEIGHT = 720
window = pyglet.window.Window(WIDTH, HEIGHT)

background_pattern = pyglet.image.SolidColorImagePattern(color=(255, 255, 255, 255))
background_image = background_pattern.create_image(WIDTH, HEIGHT)

pattern = pyglet.image.SolidColorImagePattern(color=(200, 100, 230, 255))

image = pattern.create_image(150, 2)
second = pyglet.sprite.Sprite(image, x=WIDTH // 2, y=HEIGHT // 2)

image = pattern.create_image(120, 4)
minute = pyglet.sprite.Sprite(image, x=WIDTH // 2, y=HEIGHT // 2)

image = pattern.create_image(100, 6)
hour = pyglet.sprite.Sprite(image, x=WIDTH // 2, y=HEIGHT // 2)

three = pyglet.text.Label("3", x=WIDTH // 2 + 150, y=HEIGHT // 2, font_name="Courier", font_size=30,
                          color=(0, 255, 255, 255))
six = pyglet.text.Label("6", x=WIDTH // 2, y=HEIGHT // 2 - 150, font_name="Courier", font_size=30,
                        color=(0, 255, 255, 255))
nine = pyglet.text.Label("9", x=WIDTH // 2 - 150, y=HEIGHT // 2, font_name="Courier", font_size=30,
                         color=(0, 255, 255, 255))
twelve = pyglet.text.Label("12", x=WIDTH // 2, y=HEIGHT // 2 + 150, font_name="Courier", font_size=30,
                           color=(0, 255, 255, 255))


@window.event
def on_draw():
    window.clear()
    background_image.blit(0, 0)
    second.draw()
    minute.draw()
    hour.draw()
    three.draw()
    six.draw()
    nine.draw()
    twelve.draw()


@window.event
def on_mouse_release(x, y, button, modifier):
    print(x, y, button, modifier)


def callback(dt):
    now = datetime.now()
    second.rotation = 360 * now.second / 60 - 90
    minute.rotation = 360 * now.minute / 60 - 90
    hour.rotation = 360 * (now.hour % 12 + now.minute / 60) / 24
    print(now.second, now.minute, now.hour)
    print(second.rotation, minute.rotation, hour.rotation)


pyglet.clock.schedule_interval(callback, 1 / 60)

pyglet.app.run()
