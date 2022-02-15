import pyglet


window = pyglet.window.Window()


kitten = pyglet.image.load('img.png')
kitten_stream = open('img.png', 'rb')
image_data = kitten.get_image_data()
data = image_data.get_data('RGB', kitten.width * 3)


@window.event
def on_draw():
    window.clear()
    kitten.blit(100, 100)


pyglet.app.run()
