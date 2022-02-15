import pyglet


img1 = pyglet.image.load_animation('1.gif')
img2 = pyglet.image.load_animation('img.png')
# bin = pyglet.image.atlas.TextureBin()
# animation.add_to_texture_bin(bin)
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
sprites = [pyglet.sprite.Sprite(img=img1, batch=batch, group=background),
           pyglet.sprite.Sprite(img=img2, batch=batch, group=background)]


window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.app.run()
