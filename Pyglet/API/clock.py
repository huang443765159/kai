from pyglet import clock


while 1:
    dt = clock.tick()
    print(f'FPS is {clock.get_fps()}')
