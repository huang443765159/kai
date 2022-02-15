import pyglet

# Show FPS


# The game window
class Window(pyglet.window.Window):
    def __init__(self):
        super(Window, self).__init__(vsync=False)
        self.width = 1280
        self.height = 720
        # Run "self.update" 128 frames a second and set FPS limit to 128.
        pyglet.clock.schedule_interval(self.update, 1.0 / 128.0)
        self._batch = pyglet.graphics.Batch()
        # pyglet.clock.schedule(self.update)
        # self.add_label(text='START', x=100, y=100, w=100, h=50)
        self._label = pyglet.text.Label(text='START', font_name='Arial', font_size=10,
                                        x=100, y=100, width=100, height=50,
                                        color=(0, 255, 0, 255), batch=self._batch)
        # pyglet.clock.set_fps_limit(128)
        self._fps = pyglet.window.FPSDisplay(window=self)
        self._img = pyglet.image.load('4.png')
        self._car_ship = pyglet.sprite.Sprite(img=self._img, x=0, y=-25, batch=self._batch)

    # You need the dt argument there to prevent errors,
    # it does nothing as far as I know.
    def update(self, dt):
        self._label.x += 1
        self._car_ship.x += 1

    def add_label(self, text: str, x: int, y: int, w: int, h: int):
        pass

    def on_draw(self):
        pyglet.clock.tick()  # Make sure you tick the clock!
        self.clear()
        self._batch.draw()
        self._fps.draw()


# Create a window and run
win = Window()
pyglet.app.run()
