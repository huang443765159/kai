import sdl2.ext
from sdl2 import keyboard


sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
keysym = keyboard.SDL_Keysym()
window = sdl2.ext.Window('Test', size=(640, 480))
window.show()
key_states = sdl2.SDL_GetKeyboardState(None)
key_down = False
while 1:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False
            break
    if key_states[sdl2.SDL_SCANCODE_A] and not key_down:
        print('A key pressed')
        key_down = True
    elif not key_states[sdl2.SDL_SCANCODE_A] and key_down:
        print('A key released')
        key_down = False
    window.refresh()

