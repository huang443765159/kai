import pyglet


# 在工作目录中选择一个gif动画文件
ag_file = "1.gif"
animation = pyglet.resource.animation(ag_file)
sprite = pyglet.sprite.Sprite(animation)

# 创建一个窗口并将其设置为图像大小
win = pyglet.window.Window(width=sprite.width, height=sprite.height)

# 设置窗口背景颜色 = r, g, b, alpha
# 每个值从 0.0 到 1.0
green = 0, 1, 0, 1
pyglet.gl.glClearColor(*green)


@win.event
def on_draw():
    win.clear()
    sprite.draw()


pyglet.app.run()

